# Form implementation generated from reading ui file 'UI/UIv2.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 500)
        self.Background_image = QtWidgets.QLabel(Form)
        self.Background_image.setGeometry(QtCore.QRect(0, 0, 400, 500))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Background_image.setFont(font)
        self.Background_image.setText("")
        self.Background_image.setPixmap(QtGui.QPixmap(":/newPrefix/Form2.png"))
        self.Background_image.setScaledContents(False)
        self.Background_image.setObjectName("Background_image")
        self.Confirm_Button = QtWidgets.QPushButton(Form)
        self.Confirm_Button.setGeometry(QtCore.QRect(100, 390, 187, 64))
        self.Confirm_Button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Confirm_Button.setStyleSheet("backgroun: transparent;\n"
"border: none;")
        self.Confirm_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Confirm.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Confirm_Button.setIcon(icon)
        self.Confirm_Button.setIconSize(QtCore.QSize(190, 80))
        self.Confirm_Button.setCheckable(False)
        self.Confirm_Button.setChecked(False)
        self.Confirm_Button.setAutoRepeatDelay(300)
        self.Confirm_Button.setObjectName("Confirm_Button")
        self.TextBox_Number = QtWidgets.QLineEdit(Form)
        self.TextBox_Number.setGeometry(QtCore.QRect(60, 273, 281, 41))
        self.TextBox_Number.setStyleSheet("QLineEdit {\n"
"background: transparent;\n"
"border-radius: none;\n"
"font-size: 17px;\n"
"}\n"
"\n"
"")
        self.TextBox_Number.setText("")
        self.TextBox_Number.setObjectName("TextBox_Number")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 330, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #F33;")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "!Введите данные!"))