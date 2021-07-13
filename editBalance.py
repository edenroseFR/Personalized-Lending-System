from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
import database


class EditBalance(QtWidgets.QMainWindow):
    def __init__(self, parent=None, name=None, creditorID=None, creditID=None, mode=None):
        super(EditBalance, self).__init__(parent)
        loadUi('add_or_subtract.ui', self)
        self.p = parent
        self.creditorName = name
        self.creditorID = creditorID
        self.creditID = creditID
        self.m = mode

        self.configureWidgets()

    def configureWidgets(self):
        self.attendee.addItems(database.getAttendees())
        self.pushButton.clicked.connect(self.pushButtonClicked)

        if self.m is None:
            self.pushButton.setText('Record')
        else:
            self.pushButton.setText('Update')
            self.data = database.getCreditInformation(creditID=int(self.creditID))
            index = self.attendee.findText(self.data['attendee'])
            self.attendee.setCurrentIndex(index)
            self.date.setDate(self.data['date'])
            if self.data['interest'] == 0:
                self.tabWidget.setCurrentIndex(1)
                self.itemName.setText(self.data['name'])
                self.price.setValue(self.data['amount'])
                self.quantity.setValue(self.data['quantity'])
            else:
                self.tabWidget.setCurrentIndex(0)
                self.amount.setValue(self.data['amount'])
                self.interest.setValue(self.data['interest'])


    def pushButtonClicked(self):
        self._item = self.itemName.text()
        self._qty = int(self.quantity.cleanText())
        self._price = int(self.price.cleanText())
        self._date = self.date.date().toString("yyyy-MM-dd")
        self._attendee = database.attendeeID(self.attendee.currentText())
        self._amount = int(self.amount.cleanText())
        self._interest = int(self.interest.cleanText())

        if self.m == 'e' and (self._item and self._qty and self._price) or\
           self.m == 'e' and (self._amount and self._interest):
            self.data['attendee'] = database.attendeeID(self.data['attendee'])
            database.updateCreditInfo(int(self.creditID), {'name':self._item,'quantity':self._qty,
                                                           'amount':self._price,'interest':self._interest,'date':self._date,
                                                           'attendee':self._attendee})
            self.p.fillTable(self.creditorID)
            self.close()
            return


        if self._item and self._qty and self._price:
            database.record_borrowed_item(self._item, self._qty, self._price, self._date,
                                          self.creditorID, self._attendee)

        if self._amount and self._interest:
            database.record_borrowed_money(self._amount, self._interest, self._date, self.creditorID, self._attendee)

        self.p.fillTable(self.creditorID)
        self.close()
