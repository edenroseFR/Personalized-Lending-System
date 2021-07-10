from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import database
import messagebox
import re

class AddPayment(QtWidgets.QMainWindow):
    def __init__(self,  parent=None, creditorID=None):
        super(AddPayment,self).__init__(parent)
        loadUi('add_payment.ui', self)
        self.p = parent
        self.creditorID = creditorID
        self.configureWidgets()

    def configureWidgets(self):
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.attendee.addItems(database.getAttendees())

    def pushButtonClicked(self):
        self.attendeeID = database.attendeeID(self.attendee.currentText())
        self._amount = int(self.amount.cleanText())
        self._date = self.date.date().toString("yyyy-MM-dd")

        if self._amount != 0:
            database.recordPayment(amount=self._amount, date=self._date,
                                   creditorID=self.creditorID, attendeeID=self.attendeeID)

        else:
            messagebox.emptyAmount()

        self.p.fillTable(self.creditorID)
        self.close()