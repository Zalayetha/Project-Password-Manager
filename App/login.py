from PyQt5 import QtCore, QtGui, QtWidgets
import loginResource
import sys


class Ui_Form(object):
        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(737, 625)
                Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
                self.widget = QtWidgets.QWidget(Form)
                self.widget.setGeometry(QtCore.QRect(310, 60, 301, 500))
                self.widget.setStyleSheet("background-color: rgb(26,35,50);\n"
        "border-bottom-right-radius:50px;\n"
        "/*border-top-right-radius:50px;/*")
                self.widget.setObjectName("widget")
                self.Login_Label = QtWidgets.QLabel(self.widget)
                self.Login_Label.setGeometry(QtCore.QRect(100, 60, 100, 40))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(20)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                font.setStrikeOut(False)
                font.setKerning(True)
                font.setStyleStrategy(QtGui.QFont.PreferAntialias)
                self.Login_Label.setFont(font)
                self.Login_Label.setStyleSheet("color:rgb(159,239,0);")
                self.Login_Label.setAlignment(QtCore.Qt.AlignCenter)
                self.Login_Label.setObjectName("Login_Label")
                self.inputUser = QtWidgets.QLineEdit(self.widget)
                self.inputUser.setGeometry(QtCore.QRect(60, 170, 181, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.inputUser.setFont(font)
                self.inputUser.setStyleSheet("border:none;\n"
        "color:rgb(255,255,255);\n"
        "border-bottom: 2px solid rgb();\n"
        "padding-bottom:10px;")
                self.inputUser.setObjectName("inputUser")
                self.inputPass = QtWidgets.QLineEdit(self.widget)
                self.inputPass.setGeometry(QtCore.QRect(60, 250, 181, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.inputPass.setFont(font)
                self.inputPass.setStyleSheet("border:none;\n"
        "color: rgb(255, 255, 255);\n"
        "border-bottom: 2px solid rgb();\n"
        "padding-bottom:10px;")
                self.inputPass.setObjectName("inputPass")
                self.inputPass.setEchoMode(QtWidgets.QLineEdit.Password)
                self.Login = QtWidgets.QPushButton(self.widget)
                self.Login.setGeometry(QtCore.QRect(60, 350, 200, 50))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.Login.setFont(font)
                self.Login.setStyleSheet("QPushButton#Login{\n"
        "background-color:rgb(186,255,50);\n"
        "border-radius:10px;\n"
        "color:black;\n"
        "}\n"
        "\n"
        "QPushButton#Login:hover{\n"
        "color:white;\n"
        "}\n"
        "\n"
        "QPushButton#Login:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "}\n"
        "")
                self.Login.setDefault(False)
                self.Login.setObjectName("Login")

                self.close_btn = QtWidgets.QPushButton(self.widget)
                self.close_btn.setObjectName(u"close_btn")
                self.close_btn.setGeometry(QtCore.QRect(250, 10, 41, 28))
                self.close_btn.setStyleSheet(u"QPushButton#close_btn:hover{\n"
        "	border-bottom:2px solid rgb(159,239,0);\n"
        "}")
                icon = QtGui.QIcon()
                icon.addFile(u":/Asset/img/icon_close.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.On)
                self.close_btn.setIcon(icon)
                self.close_btn.clicked.connect(lambda:self.exit())


                self.label = QtWidgets.QLabel(Form)
                self.label.setGeometry(QtCore.QRect(80, 60, 241, 501))
                self.label.setStyleSheet("border-top-left-radius:50px;\n"
        "border-image: url(:/Asset/Password Manager V4/resource file/key.png);\n"
        "/*border-bottom-left-radius:50px;/*")
                self.label.setText("")
                self.label.setScaledContents(True)
                self.label.setObjectName("label")

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.Login_Label.setText(_translate("Form", "Log In"))
                self.inputUser.setPlaceholderText(_translate("Form", "Username"))
                self.inputPass.setPlaceholderText(_translate("Form", "Password"))
                self.Login.setText(_translate("Form", "Continue"))
        
        def exit(self):
                sys.exit()

