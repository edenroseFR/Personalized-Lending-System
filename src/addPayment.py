from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import database
import messagebox

class AddPayment(QtWidgets.QMainWindow):
    def __init__(self,  parent=None, creditorID=None):
        super(AddPayment,self).__init__(parent)
        loadUi('../UI File/add_payment.ui', self)
        self.parent = parent
        self.creditorID = creditorID

        self.configureWidgets()

    def configureWidgets(self):
        self.recordButton.clicked.connect(self.tryRecordingPayment)
        self.attendee.addItems(database.getAttendees())

    def tryRecordingPayment(self):
        self.attendeeID = database.attendeeID(self.attendee.currentText())
        self.paidAmount = int(self.amount.cleanText())
        self.dateGiven = self.date.date().toString("yyyy-MM-dd")

        if self.paidAmount != 0:
            database.recordPayment(
                amount = self.paidAmount,
                date = self.dateGiven,
                creditorID = self.creditorID,
                attendeeID = self.attendeeID
            )

        else:
            messagebox.emptyAmount()

        self.parent.fillTable(self.creditorID)
        self.close()
