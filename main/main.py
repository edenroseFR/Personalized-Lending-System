import sys

from PyQt5 import QtCore, QtWidgets
from mainwin import Ui_MainWindow
from borrowersForm import Ui_MainWindow as Ui_BorrowersForm
import database as db

class MainWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listWidget.close()
        self.configureWidgets()

    def configureWidgets(self):
        self.listWidget_height = 25
        self.ui.lineEdit.textChanged.connect(self.searchResult)
        self.ui.addNewBorrower.clicked.connect(self.__gotoForm__)

    def searchResult(self):
        self.ui.listWidget.clear()
        if self.ui.lineEdit.hasFocus():
            chars = self.ui.lineEdit.text()
            updated_names = db.searched_names(key=chars)
            self.ui.listWidget.addItems(updated_names)
            self.ui.listWidget.setGeometry(QtCore.QRect(160, 250, 451, self.listWidget_height*(len(updated_names)))) # updates listWidget's height depending on the name that matches
            self.ui.listWidget.show()

            self.ui.listWidget.itemClicked.connect(self.itemSelected)

        if self.ui.lineEdit.text() == '':
            self.ui.listWidget.close()

    def itemSelected(self, row):
        print(row.text())

    def __gotoForm__(self):
        self.goto = BorrowersForm()
        self.goto.show()

class BorrowersForm(QtWidgets.QMainWindow, Ui_BorrowersForm):
    def __init__(self):
        super().__init__()

        self.ui = Ui_BorrowersForm()
        self.ui.setupUi(self)
        self.configureWidgets()

    def configureWidgets(self):
        self.ui.form.setCurrentIndex(0)

        self.ui.nextButton_4.clicked.connect(self.nextPage)
        self.ui.nextButton_3.clicked.connect(self.nextPage)
        self.ui.nextButton_2.clicked.connect(self.nextPage)
        self.ui.nextButton.clicked.connect(self.nextPage)

        self.ui.prevButton_4.clicked.connect(self.prevPage)
        self.ui.prevButton_3.clicked.connect(self.prevPage)
        self.ui.prevButton_2.clicked.connect(self.prevPage)
        self.ui.prevButton.clicked.connect(self.prevPage)


    def nextPage(self):
        self.currentIndex = self.ui.form.currentIndex()
        self.ui.form.setCurrentIndex(self.currentIndex+1)
        if self.currentIndex != 5:
            self.currentIndex += 1

    def prevPage(self):
        self.currentIndex = self.ui.form.currentIndex()
        self.ui.form.setCurrentIndex(self.currentIndex-1)
        if self.currentIndex != 0:
            self.currentIndex -= 1










app = QtWidgets.QApplication(sys.argv)
win = MainWin()
win.show()
sys.exit(app.exec_())
