from PyQt5.QtWidgets import QMessageBox

def incompleteField(parent=None):
    return QMessageBox.information(parent,'Borrower', 'Please fill up all the fields in the Borrowers tab.')

def debtBoxIncomplete(parent=None):
    return QMessageBox.information(parent,'Incomplete Fields', 'Please fill up all the fields in Money or Item tab.')

def confirmDelete(parent=None):
    prompt = QMessageBox.warning(parent, 'Confirm Deletion', 'This action cannot be undone.\nAre you sure you want to delete this item ?', QMessageBox.Ok, QMessageBox.Cancel)
    if prompt == QMessageBox.Ok:
        return True
