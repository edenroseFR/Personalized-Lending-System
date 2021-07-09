from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 398)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.form = QtWidgets.QStackedWidget(self.centralwidget)
        self.form.setEnabled(True)
        self.form.setGeometry(QtCore.QRect(20, 10, 291, 381))
        self.form.setStyleSheet("#prevButton{\n"
        "background-color: TRANSPARENT;\n"
        "border: TRANSPARENT;\n"
        "}")
        self.form.setObjectName("form")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.userpic = QtWidgets.QPushButton(self.page)
        self.userpic.setEnabled(True)
        self.userpic.setGeometry(QtCore.QRect(10, 120, 61, 121))
        self.userpic.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userpic.setIcon(icon)
        self.userpic.setIconSize(QtCore.QSize(100, 100))
        self.userpic.setFlat(True)
        self.userpic.setObjectName("userpic")
        self.rect1 = QtWidgets.QWidget(self.page)
        self.rect1.setGeometry(QtCore.QRect(70, 130, 211, 31))
        self.rect1.setStyleSheet("#rect1{\n"
        "background-color:  white;\n"
        "border: 1px solid  #fc5404;\n"
        "border-radius: 15px;\n"
        "}")
        self.rect1.setObjectName("rect1")
        self.first_name = QtWidgets.QLineEdit(self.rect1)
        self.first_name.setGeometry(QtCore.QRect(10, 5, 191, 20))
        self.first_name.setStyleSheet("#first_name{\n"
        "border: 1px solid white;\n"
        "}")
        self.first_name.setObjectName("first_name")
        self.rect2 = QtWidgets.QWidget(self.page)
        self.rect2.setGeometry(QtCore.QRect(20, 270, 261, 31))
        self.rect2.setStyleSheet("#rect2{\n"
        "background-color:  white;\n"
        "border: 1px solid  #fc5404;\n"
        "border-radius: 15px;\n"
        "}")
        self.rect2.setObjectName("rect2")
        self.address = QtWidgets.QLineEdit(self.rect2)
        self.address.setGeometry(QtCore.QRect(10, 5, 241, 20))
        self.address.setStyleSheet("#address{\n"
        "border: 1px solid white;\n"
        "}")
        self.address.setObjectName("address")
        self.rect3 = QtWidgets.QWidget(self.page)
        self.rect3.setGeometry(QtCore.QRect(20, 310, 261, 31))
        self.rect3.setStyleSheet("#rect3{\n"
        "background-color:  white;\n"
        "border: 1px solid  #fc5404;\n"
        "border-radius: 15px;\n"
        "}")
        self.rect3.setObjectName("rect3")
        self.contact = QtWidgets.QLineEdit(self.rect3)
        self.contact.setGeometry(QtCore.QRect(10, 5, 241, 20))
        self.contact.setStyleSheet("#contact{\n"
        "border: 1px solid white;\n"
        "}")
        self.contact.setObjectName("contact")
        self.header = QtWidgets.QWidget(self.page)
        self.header.setGeometry(QtCore.QRect(-7, -40, 301, 141))
        self.header.setStyleSheet("#header{\n"
        "background-color:  #fc5404;\n"
        "border: 1px solid  #fc5404;\n"
        "border-radius: 30px;\n"
        "}")
        self.header.setObjectName("header")
        self.label = QtWidgets.QLabel(self.header)
        self.label.setGeometry(QtCore.QRect(40, 90, 231, 31))
        self.label.setStyleSheet("#label{\n"
        "color: white;\n"
        "font: 25 26pt \"Bodoni MT Poster Compressed\";\n"
        "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.rect1_2 = QtWidgets.QWidget(self.page)
        self.rect1_2.setGeometry(QtCore.QRect(70, 170, 211, 31))
        self.rect1_2.setStyleSheet("#rect1{\n"
        "background-color:  white;\n"
        "border: 1px solid  #fc5404;\n"
        "border-radius: 15px;\n"
        "}")
        self.rect1_2.setObjectName("rect1_2")
        self.name_2 = QtWidgets.QLineEdit(self.rect1_2)
        self.name_2.setGeometry(QtCore.QRect(10, 5, 191, 20))
        self.name_2.setStyleSheet("#name{\n"
        "border: 1px solid white;\n"
        "}")
        self.name_2.setObjectName("name_2")
        self.rect1_3 = QtWidgets.QWidget(self.rect1_2)
        self.rect1_3.setGeometry(QtCore.QRect(0, 0, 211, 31))
        self.rect1_3.setStyleSheet("#rect1_3{\n"
        "background-color:  white;\n"
        "border: 1px solid  #fc5404;\n"
        "border-radius: 15px;\n"
        "}")
        self.rect1_3.setObjectName("rect1_3")
        self.middle_name = QtWidgets.QLineEdit(self.rect1_3)
        self.middle_name.setGeometry(QtCore.QRect(10, 5, 191, 20))
        self.middle_name.setStyleSheet("#middle_name{\n"
        "border: 1px solid white;\n"
        "}")
        self.middle_name.setObjectName("middle_name")
        self.rect1_4 = QtWidgets.QWidget(self.page)
        self.rect1_4.setGeometry(QtCore.QRect(70, 210, 211, 31))
        self.rect1_4.setStyleSheet("#rect1_4{\n"
        "background-color:  white;\n"
        "border: 1px solid  #fc5404;\n"
        "border-radius: 15px;\n"
        "}")
        self.rect1_4.setObjectName("rect1_4")
        self.last_name = QtWidgets.QLineEdit(self.rect1_4)
        self.last_name.setGeometry(QtCore.QRect(10, 5, 191, 20))
        self.last_name.setStyleSheet("#last_name{\n"
        "border: 1px solid white;\n"
        "}")
        self.last_name.setObjectName("last_name")
        self.nextButton_4 = QtWidgets.QPushButton(self.page)
        self.nextButton_4.setGeometry(QtCore.QRect(250, 349, 41, 31))
        self.nextButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton_4.setStyleSheet("#nextButton_4 {\n"
        "background-color: TRANSPARENT;\n"
        "border: TRANSPARENT;\n"
        "}")
        self.nextButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../img/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton_4.setIcon(icon1)
        self.nextButton_4.setIconSize(QtCore.QSize(30, 30))
        self.nextButton_4.setObjectName("nextButton_4")
        self.prevButton_4 = QtWidgets.QPushButton(self.page)
        self.prevButton_4.setGeometry(QtCore.QRect(220, 350, 31, 31))
        self.prevButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prevButton_4.setStyleSheet("#prevButton_4 {\n"
        "background-color: TRANSPARENT;\n"
        "border: TRANSPARENT;\n"
        "}")
        self.prevButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../img/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevButton_4.setIcon(icon2)
        self.prevButton_4.setIconSize(QtCore.QSize(30, 30))
        self.prevButton_4.setObjectName("prevButton_4")
        self.form.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.header2 = QtWidgets.QWidget(self.page_2)
        self.header2.setGeometry(QtCore.QRect(-7, -40, 301, 141))
        self.header2.setStyleSheet("#header2{\n"
        "background-color:  #fc5404;\n"
        "border: 1px solid  #fc5404;\n"
        "border-radius: 30px;\n"
        "}")
        self.header2.setObjectName("header2")
        self.label2 = QtWidgets.QLabel(self.header2)
        self.label2.setGeometry(QtCore.QRect(40, 90, 231, 31))
        self.label2.setStyleSheet("#label2{\n"
        "color: white;\n"
        "font: 25 26pt \"Bodoni MT Poster Compressed\";\n"
        "}")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.rect3_p2 = QtWidgets.QWidget(self.page_2)
        self.rect3_p2.setGeometry(QtCore.QRect(20, 190, 251, 31))
        self.rect3_p2.setStyleSheet("#rect3_p2{\n"
        "background-color:  white;\n"
        "border: 2px solid  #fc5404;\n"
        "border-radius: 15px;\n"
        "}")
        self.rect3_p2.setObjectName("rect3_p2")
        self.total = QtWidgets.QLineEdit(self.rect3_p2)
        self.total.setGeometry(QtCore.QRect(10, 5, 231, 20))
        self.total.setStyleSheet("#total{\n"
        "border: 1px solid white;\n"
        "    font: 75 12pt \"MS Shell Dlg 2\";\n"
        "}")
        self.total.setAlignment(QtCore.Qt.AlignCenter)
        self.total.setPlaceholderText("")
        self.total.setObjectName("total")
        self.rect1_p2 = QtWidgets.QWidget(self.page_2)
        self.rect1_p2.setGeometry(QtCore.QRect(20, 130, 131, 31))
        self.rect1_p2.setStyleSheet("#rect1_p2{\n"
        "background-color:  white;\n"
        "border: 1px solid  #fc5404;\n"
        "border-radius: 15px;\n"
        "}")
        self.rect1_p2.setObjectName("rect1_p2")
        self.amount = QtWidgets.QSpinBox(self.rect1_p2)
        self.amount.setGeometry(QtCore.QRect(10, 4, 111, 22))
        self.amount.setStyleSheet("#amount{\n"
        "border: 1px solid white;\n"
        "}")
        self.amount.setMaximum(1000000)
        self.amount.setObjectName("amount")
        self.rect4_p2 = QtWidgets.QWidget(self.page_2)
        self.rect4_p2.setGeometry(QtCore.QRect(20, 250, 251, 31))
        self.rect4_p2.setStyleSheet("#rect4_p2{\n"
        "background-color:  white;\n"
        "border: 1px solid  #fc5404;\n"
        "\n"
        "}")
        self.rect4_p2.setObjectName("rect4_p2")
        self.cashier = QtWidgets.QComboBox(self.rect4_p2)
        self.cashier.setGeometry(QtCore.QRect(5, 4, 241, 22))
        self.cashier.setStyleSheet("#cashier{\n"
        "background-color: white;\n"
        "border: 1px solid white;\n"
        "}")
        self.cashier.setObjectName("cashier")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 47, 13))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(160, 110, 101, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.rect2_p2 = QtWidgets.QWidget(self.page_2)
        self.rect2_p2.setGeometry(QtCore.QRect(160, 130, 101, 31))
        self.rect2_p2.setStyleSheet("#rect1_p2{\n"
        "background-color:  white;\n"
        "border: 1px solid  #fc5404;\n"
        "border-radius: 15px;\n"
        "}")
        self.rect2_p2.setObjectName("rect2_p2")
        self.percentage = QtWidgets.QSpinBox(self.rect2_p2)
        self.percentage.setGeometry(QtCore.QRect(10, 4, 81, 22))
        self.percentage.setStyleSheet("#amount{\n"
        "border: 1px solid white;\n"
        "}")
        self.percentage.setSuffix("")
        self.percentage.setMaximum(1000000)
        self.percentage.setObjectName("percentage")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 251, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 251, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.date = QtWidgets.QDateTimeEdit(self.page_2)
        self.date.setGeometry(QtCore.QRect(20, 310, 121, 22))
        self.date.setCalendarPopup(True)
        self.date.setTimeSpec(QtCore.Qt.TimeZone)
        self.date.setObjectName("date")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(20, 290, 121, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.duedate = QtWidgets.QDateTimeEdit(self.page_2)
        self.duedate.setGeometry(QtCore.QRect(150, 310, 121, 22))
        self.duedate.setWrapping(False)
        self.duedate.setFrame(True)
        self.duedate.setCalendarPopup(True)
        self.duedate.setObjectName("duedate")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(150, 290, 121, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.nextButton = QtWidgets.QPushButton(self.page_2)
        self.nextButton.setGeometry(QtCore.QRect(250, 350, 41, 31))
        self.nextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton.setStyleSheet("#nextButton {\n"
        "background-color: TRANSPARENT;\n"
        "border: TRANSPARENT;\n"
        "}")
        self.nextButton.setText("")
        self.nextButton.setIcon(icon1)
        self.nextButton.setIconSize(QtCore.QSize(30, 30))
        self.nextButton.setObjectName("nextButton")
        self.prevButton = QtWidgets.QPushButton(self.page_2)
        self.prevButton.setGeometry(QtCore.QRect(220, 351, 31, 31))
        self.prevButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prevButton.setText("")
        self.prevButton.setIcon(icon2)
        self.prevButton.setIconSize(QtCore.QSize(30, 30))
        self.prevButton.setObjectName("prevButton")
        self.form.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.rect1_p3 = QtWidgets.QWidget(self.page_3)
        self.rect1_p3.setGeometry(QtCore.QRect(11, 110, 271, 31))
        self.rect1_p3.setStyleSheet("#rect1_p3{\n"
        "background-color:  white;\n"
        "border: 1px solid  #fc5404;\n"
        "border-radius: 15px;\n"
        "}")
        self.rect1_p3.setObjectName("rect1_p3")
        self.itemName = QtWidgets.QLineEdit(self.rect1_p3)
        self.itemName.setGeometry(QtCore.QRect(10, 5, 251, 20))
        self.itemName.setStyleSheet("#itemName{\n"
        "border: 1px solid white;\n"
        "}")
        self.itemName.setObjectName("itemName")
        self.header3 = QtWidgets.QWidget(self.page_3)
        self.header3.setGeometry(QtCore.QRect(-7, -40, 301, 141))
        self.header3.setStyleSheet("#header3{\n"
        "background-color:  #fc5404;\n"
        "border: 1px solid  #fc5404;\n"
        "border-radius: 30px;\n"
        "}")
        self.header3.setObjectName("header3")
        self.label3 = QtWidgets.QLabel(self.header3)
        self.label3.setGeometry(QtCore.QRect(40, 90, 231, 31))
        self.label3.setStyleSheet("#label3{\n"
        "color: white;\n"
        "font: 25 26pt \"Bodoni MT Poster Compressed\";\n"
        "}")
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.quantity = QtWidgets.QDoubleSpinBox(self.page_3)
        self.quantity.setGeometry(QtCore.QRect(35, 160, 101, 22))
        self.quantity.setSuffix("")
        self.quantity.setObjectName("quantity")
        self.label1_p3 = QtWidgets.QLabel(self.page_3)
        self.label1_p3.setGeometry(QtCore.QRect(35, 140, 101, 20))
        self.label1_p3.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_p3.setObjectName("label1_p3")
        self.quantity_2 = QtWidgets.QDoubleSpinBox(self.page_3)
        self.quantity_2.setGeometry(QtCore.QRect(160, 160, 101, 22))
        self.quantity_2.setObjectName("quantity_2")
        self.label1_p3_2 = QtWidgets.QLabel(self.page_3)
        self.label1_p3_2.setGeometry(QtCore.QRect(160, 140, 101, 20))
        self.label1_p3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_p3_2.setObjectName("label1_p3_2")
        self.label3_p3 = QtWidgets.QLabel(self.page_3)
        self.label3_p3.setGeometry(QtCore.QRect(20, 190, 251, 20))
        self.label3_p3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_p3.setObjectName("label3_p3")
        self.rect3_p3 = QtWidgets.QWidget(self.page_3)
        self.rect3_p3.setGeometry(QtCore.QRect(20, 210, 251, 31))
        self.rect3_p3.setStyleSheet("#rect3_p3{\n"
        "background-color:  white;\n"
        "border: 2px solid  #fc5404;\n"
        "border-radius: 15px;\n"
        "}")
        self.rect3_p3.setObjectName("rect3_p3")
        self.total_p3 = QtWidgets.QLineEdit(self.rect3_p3)
        self.total_p3.setGeometry(QtCore.QRect(10, 5, 231, 20))
        self.total_p3.setStyleSheet("#total_p3{\n"
        "border: 1px solid white;\n"
        "    font: 75 12pt \"MS Shell Dlg 2\";\n"
        "}")
        self.total_p3.setAlignment(QtCore.Qt.AlignCenter)
        self.total_p3.setPlaceholderText("")
        self.total_p3.setObjectName("total_p3")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(20, 240, 251, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.date_2 = QtWidgets.QDateTimeEdit(self.page_3)
        self.date_2.setGeometry(QtCore.QRect(20, 320, 121, 22))
        self.date_2.setCalendarPopup(True)
        self.date_2.setTimeSpec(QtCore.Qt.TimeZone)
        self.date_2.setObjectName("date_2")
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setGeometry(QtCore.QRect(150, 300, 121, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(20, 300, 121, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.rect4_p3 = QtWidgets.QWidget(self.page_3)
        self.rect4_p3.setGeometry(QtCore.QRect(20, 260, 251, 31))
        self.rect4_p3.setStyleSheet("#rect4_p3{\n"
        "background-color:  white;\n"
        "border: 1px solid  #fc5404;\n"
        "\n"
        "}")
        self.rect4_p3.setObjectName("rect4_p3")
        self.cashier_p3 = QtWidgets.QComboBox(self.rect4_p3)
        self.cashier_p3.setGeometry(QtCore.QRect(5, 5, 241, 22))
        self.cashier_p3.setStyleSheet("#cashier_p3{\n"
        "background-color: white;\n"
        "border: 1px solid white;\n"
        "}")
        self.cashier_p3.setObjectName("cashier_p3")
        self.duedate_2 = QtWidgets.QDateTimeEdit(self.page_3)
        self.duedate_2.setGeometry(QtCore.QRect(150, 320, 121, 22))
        self.duedate_2.setWrapping(False)
        self.duedate_2.setFrame(True)
        self.duedate_2.setCalendarPopup(True)
        self.duedate_2.setObjectName("duedate_2")
        self.prevButton_2 = QtWidgets.QPushButton(self.page_3)
        self.prevButton_2.setGeometry(QtCore.QRect(220, 350, 31, 31))
        self.prevButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prevButton_2.setStyleSheet("#prevButton_2 {\n"
        "background-color: TRANSPARENT;\n"
        "border: TRANSPARENT;\n"
        "}")
        self.prevButton_2.setText("")
        self.prevButton_2.setIcon(icon2)
        self.prevButton_2.setIconSize(QtCore.QSize(30, 30))
        self.prevButton_2.setObjectName("prevButton_2")
        self.nextButton_2 = QtWidgets.QPushButton(self.page_3)
        self.nextButton_2.setGeometry(QtCore.QRect(250, 349, 41, 31))
        self.nextButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton_2.setStyleSheet("#nextButton_2 {\n"
"background-color: TRANSPARENT;\n"
"border: TRANSPARENT;\n"
"}")
        self.nextButton_2.setText("")
        self.nextButton_2.setIcon(icon1)
        self.nextButton_2.setIconSize(QtCore.QSize(30, 30))
        self.nextButton_2.setObjectName("nextButton_2")
        self.form.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.bg_4 = QtWidgets.QWidget(self.page_4)
        self.bg_4.setGeometry(QtCore.QRect(0, 0, 301, 381))
        self.bg_4.setStyleSheet("#bg_4{\n"
"background-color:  #fc5404;\n"
"}")
        self.bg_4.setObjectName("bg_4")
        self.submitButton = QtWidgets.QPushButton(self.bg_4)
        self.submitButton.setGeometry(QtCore.QRect(60, 260, 161, 31))
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setStyleSheet("#submitButton{\n"
"background-color: white;\n"
"border: 1px solid white;\n"
"border-radius: 15px;\n"
"}")
        self.submitButton.setObjectName("submitButton")
        self.cancelButton = QtWidgets.QPushButton(self.bg_4)
        self.cancelButton.setGeometry(QtCore.QRect(60, 300, 161, 31))
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet("#cancelButton{\n"
"color: white;\n"
"background-color: #fc5404;;\n"
"border: 1px solid white;\n"
"border-radius: 15px;\n"
"}")
        self.cancelButton.setObjectName("cancelButton")
        self.namePreview = QtWidgets.QLabel(self.bg_4)
        self.namePreview.setGeometry(QtCore.QRect(20, 60, 261, 31))
        self.namePreview.setStyleSheet("#namePreview{\n"
"color: white;\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.namePreview.setObjectName("namePreview")
        self.detailsPreview1 = QtWidgets.QLabel(self.bg_4)
        self.detailsPreview1.setGeometry(QtCore.QRect(20, 90, 261, 131))
        self.detailsPreview1.setStyleSheet("#detailsPreview{\n"
"color: white;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.detailsPreview1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.detailsPreview1.setObjectName("detailsPreview1")
        self.detailsPreview2_2 = QtWidgets.QLabel(self.bg_4)
        self.detailsPreview2_2.setGeometry(QtCore.QRect(20, -3, 61, 31))
        self.detailsPreview2_2.setStyleSheet("#detailsPreview{\n"
"color: white;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.detailsPreview2_2.setObjectName("detailsPreview2_2")
        self.nextButton_3 = QtWidgets.QPushButton(self.page_4)
        self.nextButton_3.setGeometry(QtCore.QRect(250, 349, 41, 31))
        self.nextButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton_3.setStyleSheet("#nextButton_3{\n"
"background-color: TRANSPARENT;\n"
"border: TRANSPARENT;\n"
"}")
        self.nextButton_3.setText("")
        self.nextButton_3.setIcon(icon1)
        self.nextButton_3.setIconSize(QtCore.QSize(30, 30))
        self.nextButton_3.setObjectName("nextButton_3")
        self.prevButton_3 = QtWidgets.QPushButton(self.page_4)
        self.prevButton_3.setGeometry(QtCore.QRect(220, 350, 31, 31))
        self.prevButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prevButton_3.setStyleSheet("#prevButton_3 {\n"
"background-color: TRANSPARENT;\n"
"border: TRANSPARENT;\n"
"}")
        self.prevButton_3.setText("")
        self.prevButton_3.setIcon(icon2)
        self.prevButton_3.setIconSize(QtCore.QSize(30, 30))
        self.prevButton_3.setObjectName("prevButton_3")
        self.form.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.form.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Customer Form"))
        self.first_name.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.address.setPlaceholderText(_translate("MainWindow", "Purok, Barangay, Municipality, Province"))
        self.contact.setPlaceholderText(_translate("MainWindow", "Contact #"))
        self.label.setText(_translate("MainWindow", "Borrower"))
        self.name_2.setPlaceholderText(_translate("MainWindow", "First, Middle,"))
        self.middle_name.setPlaceholderText(_translate("MainWindow", "Middle Name"))
        self.last_name.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.label2.setText(_translate("MainWindow", "Borrowed Cash"))
        self.amount.setSuffix(_translate("MainWindow", ".00"))
        self.amount.setPrefix(_translate("MainWindow", "P "))
        self.label_2.setText(_translate("MainWindow", "Amount"))
        self.label_3.setText(_translate("MainWindow", "Percentage"))
        self.percentage.setPrefix(_translate("MainWindow", "% 0."))
        self.label_4.setText(_translate("MainWindow", "Total Payable"))
        self.label_5.setText(_translate("MainWindow", "Cashier"))
        self.label_6.setText(_translate("MainWindow", "Date"))
        self.label_7.setText(_translate("MainWindow", "Due Date"))
        self.itemName.setPlaceholderText(_translate("MainWindow", "Item"))
        self.label3.setText(_translate("MainWindow", "Borrowed Item"))
        self.quantity.setPrefix(_translate("MainWindow", "P "))
        self.label1_p3.setText(_translate("MainWindow", "Price"))
        self.label1_p3_2.setText(_translate("MainWindow", "Quantity"))
        self.label3_p3.setText(_translate("MainWindow", "Total Payable"))
        self.label_8.setText(_translate("MainWindow", "Cashier"))
        self.label_9.setText(_translate("MainWindow", "Due Date"))
        self.label_10.setText(_translate("MainWindow", "Date"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.namePreview.setText(_translate("MainWindow", "Name: Monica Gastambidi"))
        self.detailsPreview1.setText(_translate("MainWindow", "01/25/2021 - P 1000.00\n"
"Cash\n"
"01/25/2021 - P200.00\n"
"Items"))
        self.detailsPreview2_2.setText(_translate("MainWindow", "> PREVIEW"))
