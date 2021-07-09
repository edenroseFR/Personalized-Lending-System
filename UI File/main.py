import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
from editBalance import EditBalance
import database
import messagebox
import re

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi('mainwin.ui', self)
        self.listWidget.close()
        self.configureWidgets()

    def configureWidgets(self):
        self.listWidget_height = 25
        self.lineEdit.textChanged.connect(self.fieldPressed)
        self.addNewUser.clicked.connect(self.addNewPressed)
        self.creditorsButton.clicked.connect(self.creditorsPressed)

    def fieldPressed(self):
        self.listWidget.clear()
        if self.lineEdit.hasFocus():
            characters = self.lineEdit.text()
            self.updated_names = database.searched_names(key=characters)
            names = [re.sub("[^A-Z a-z^.]", "", i) for i in self.updated_names]
            self.listWidget.addItems(names)
            self.listWidget.setGeometry(QtCore.QRect(160,250,451,self.listWidget_height*(len(self.updated_names))))
            self.listWidget.show()

            self.listWidget.itemClicked.connect(self.itemClicked)


    def addNewPressed(self):
        self.newWin = NewCreditor()
        self.newWin.show()


    def itemClicked(self, item):
        selected = [re.sub("[^0-9^.]", "", i) for i in self.updated_names if re.sub("[^A-Z a-z^.]", "", i) == item.text()]
        self.newWin = BalanceSheet(name = item.text(), id = int(selected[0]))
        self.newWin.show()
        self.close()


    def creditorsPressed(self):
        self.newWin = BorrowersTable()
        self.newWin.show()
        self.close()


class BalanceSheet(QtWidgets.QMainWindow):
    def __init__(self, name=None, id=None):
        super(BalanceSheet,self).__init__()
        loadUi('balance_sheet.ui', self)

        self.lendee = name
        self.id = id
        self.lendee_address = database.get_address(person=self.id)
        self.fillTable(self.id)
        self.configureWidgets()

    def configureWidgets(self):
        self.home.clicked.connect(self.homeClicked)
        self.addButton.clicked.connect(self.addButtonClicked)
        self.deleteButton.clicked.connect(self.deleteButtonClicked)
        self.name.setText(self.lendee)
        self.purok.setText(self.lendee_address)
        self.tableWidget.itemDoubleClicked.connect(self.doubleClicked)

    def doubleClicked(self):
        id = self.tableWidget.item(self.tableWidget.currentRow(),0).text()
        self.newWin = self.newWin = EditBalance(parent=self, creditorID=self.id, creditID=id, mode='e')
        self.newWin.show()

    def fillTable(self, ID):
        self.tableWidget.setRowCount(0)
        row = 0
        self.activities = database.creditorHistory(ID)
        self.tableWidget.setRowCount(len(self.activities))

        for activity in self.activities:
            if isinstance(activity[1], str):
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(activity[0])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(activity[1])))
                self.tableWidget.setItem(row, 2, QTableWidgetItem('+'))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(activity[2])))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(str(activity[3])))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(str(activity[4])))
            row += 1

    def homeClicked(self):
        self.newWin = MainWindow()
        self.newWin.show()
        self.close()

    def addButtonClicked(self):
        self.newWin = EditBalance(self, self.lendee, self.id)
        self.newWin.show()

    def deleteButtonClicked(self):
        if messagebox.confirmDelete(self):
            creditID = self.tableWidget.item(self.tableWidget.currentRow(),0).text()
            database.deleteCredit(int(creditID))

        self.fillTable(self.id)



    def pushButtonClicked(self):
        self._item = self.itemName.text()
        self._qty = int(self.quantity.cleanText())
        self._price = int(self.price.cleanText())
        self._date = self.date.date().toString("yyyy-MM-dd")
        self._attendee = database.attendeeID(self.attendee.currentText())
        self._amount = int(self.amount.cleanText())
        self._interest = int(self.interest.cleanText())

        if self._item and self._qty and self._price:
            print(self._item,self._qty,self._price,self._date,self.creditorID,self._attendee)
            database.record_borrowed_item(self._item, self._qty, self._price, self._date,
                                          self.creditorID,self._attendee)

        if self._amount and self._interest:
            database.record_borrowed_money(self._amount, self._interest, self._date, self.creditorID, self._attendee)


        self.p.fillTable(self.creditorID)
        self.close()




class NewCreditor(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('add_creditor.ui', self)
        self.configureWidgets()

    def configureWidgets(self):
        self.attendee.addItems(database.getAttendees())
        self.pushButton.clicked.connect(self.pushButtonClicked)


    def pushButtonClicked(self):
        self.first = self.first_name.text()
        self.middle = self.middle_name.text()
        self.last = self.last_name.text()
        self.purok = self.purok.text()
        self.barangay = self.barangay.text()
        self.municipality = self.municipality.text()
        self._amount = int(self.amount.cleanText())
        self._interest = int(self.interest.cleanText())
        self._itemName = self.itemName.text()
        self._quantity = self.quantity.cleanText()
        self._price = self.price.cleanText()
        self._attendee = self.attendee.currentText()
        self._date = self.date.date().toString("yyyy-MM-dd")

        if self.first and self.last and self.purok and self.barangay and self.municipality:
            if (self._amount != '0' and self._interest) or (self._itemName and self._quantity and self._price):
                self.recordCreditor()
            else:
                messagebox.debtBoxIncomplete(self)
        else:
            messagebox.incompleteField(self)



    def recordCreditor(self):
        database.addCreditor(self.first,self.middle,self.last,self.purok,self.barangay,self.municipality)
        self.recordCredit()

    def recordCredit(self):
        if self._amount != '0' and self._interest:
            database.record_borrowed_money(self._amount, self._interest, self._date,
                                           database.lastInsertedID(), database.attendeeID(self._attendee))
        if self._itemName and self._quantity and self._price:
            database.record_borrowed_item(self._itemName, self._quantity, self._price, self._date,
                                          database.lastInsertedID(), database.attendeeID(self._attendee))

        self.close()


class BorrowersTable(QtWidgets.QMainWindow):
    def __init__(self):
        super(BorrowersTable,self).__init__()
        loadUi('borrowers.ui', self)
        self.configureWidgets()

    def configureWidgets(self):
        self.fillTable()

        self.home.clicked.connect(self.homeClicked)

    def fillTable(self):
        self.tableWidget.setRowCount(0)
        self.data = database.creditors_balance()
        self.tableWidget.setRowCount(database.allCreditors())

        row = 0
        for i in self.data:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(i[2])))

            row += 1




    def homeClicked(self):
        self.newWin = MainWindow()
        self.newWin.show()
        self.close()



app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())