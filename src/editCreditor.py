from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import database
import messagebox



class EditCreditor(QtWidgets.QMainWindow):
    def __init__(self, parent=None, creditorID=None):
        super(EditCreditor, self).__init__(parent)
        loadUi('../UI File/edit_creditor.ui', self)

        self.p = parent
        self.id = creditorID
        self.data = database.getCreditorInformation(self.id)

        self.configureWidgets()

    def configureWidgets(self):
        self.first_name.setText(self.data[1])
        self.middle_name.setText(self.data[2])
        self.last_name.setText(self.data[3])
        self.purok.setText(self.data[4])
        self.barangay.setText(self.data[5])
        self.municipality.setText(self.data[6])

        self.pushButton.clicked.connect(self.pushButtonClicked)

    def pushButtonClicked(self):
        self.newData = {
            'first': self.first_name.text(),
            'middle': self.middle_name.text(),
            'last': self.last_name.text(),
            'purok': self.purok.text(),
            'barangay': self.barangay.text(),
            'municipality': self.municipality.text()
        }
        database.updateCreditorInformation(self.id, self.newData)
        messagebox.creditorUpdated(self)
        self.close()
        self.p.fillTable()
