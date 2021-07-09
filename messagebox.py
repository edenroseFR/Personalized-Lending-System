from PyQt5.QtWidgets import QMessageBox

def incompleteField(parent=None):
    return QMessageBox.information(parent,'Borrower', 'Please fill up all the fields in the Borrowers tab.')

def debtBoxIncomplete(parent=None):
    return QMessageBox.information(parent,'Incomplete Fields', 'Please fill up all the fields in Money or Item tab.')