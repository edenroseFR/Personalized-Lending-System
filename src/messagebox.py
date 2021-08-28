import PyQt5
from PyQt5.QtWidgets import QMessageBox

def incompleteField(parent=None):
    return QMessageBox.information(parent,
                                   'Borrower',
                                   'Please fill up all the fields in the Borrowers tab.')

def debtBoxIncomplete(parent=None):
    return QMessageBox.information(parent,
                                   'Incomplete Fields',
                                   'Please fill up all the fields in Money or Item tab.')

def confirmDelete(parent=None):
    prompt = QMessageBox.warning(parent,
                                 'Confirm Deletion',
                                 'This action cannot be undone.\nAre you sure you want to proceed?',
                                 QMessageBox.Ok, QMessageBox.Cancel)
    if prompt == QMessageBox.Ok:
        return True

def confirmDeleteCreditor(parent=None, fullName=None):
    prompt = QMessageBox.warning(parent, 'Confirm Deletion',
                                 'This action cannot be undone.\nAre you sure you want to delete %s ?'%fullName,
                                 QMessageBox.Ok, QMessageBox.Cancel)
    if prompt == QMessageBox.Ok:
        return True

def creditorUpdated(parent=None):
    return QMessageBox.information(parent, 'Update',
                                   'Creditor Information updated successfully.')

def emptyAmount(parent=None):
    return QMessageBox.warning(parent, 'Payment', 'Amount cannot be zero.')

def selectBorrower(parent=None):
    return QMessageBox.warning(parent, 'Edit', 'Please select a row first.')

def cantDelete(parent=None):
    return QMessageBox.information(parent, 'Delete',
                                   'Oops! You cannot delete a creditor who has not fully paid yet')

def noResultFound(parent=None):
    return QMessageBox.information(parent, 'Search Result', 'No result found.')

def messageSent(parent=None):
    return QMessageBox.information(parent, 'Lending Co.',
                                   'Message recieved!\nWe will reply via email.')

def messageNotSent(parent=None):
    return QMessageBox.information(parent, 'Lending Co.',
                                   'Sorry, we are unable to send your message.\nPlease check your internet connection.')

def invalidEmail(parent=None):
    return QMessageBox.information(parent, 'Lending Co.',
                                   'Sending failed.\nYou entered an invalid email address.')

def emptyContent(parent=None):
    return QMessageBox.information(parent, 'Lending Co.',
                                   'Sending failed.\nWe do not accept empty content.')
