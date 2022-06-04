from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import resource

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1238, 720)
                MainWindow.setStyleSheet("background-color: rgb(20, 29, 43);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName("verticalLayout")

                # top bar
                self.topBar = QtWidgets.QFrame(self.centralwidget)
                self.topBar.setMaximumSize(QtCore.QSize(16777215, 50))
                self.topBar.setStyleSheet("background-color: rgb(17, 25, 39);")
                self.topBar.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.topBar.setFrameShadow(QtWidgets.QFrame.Raised)
                self.topBar.setObjectName("topBar")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.topBar)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setSpacing(0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                
                # menu button
                self.menu_btn = QtWidgets.QFrame(self.topBar)
                self.menu_btn.setMaximumSize(QtCore.QSize(80, 16777215))
                self.menu_btn.setStyleSheet("QFrame#menu_btn{\n"
        "background-color: rgb(17, 25, 39);\n"
        "}\n"
        "QFrame#menu_btn:hover{\n"
        "    border-bottom:4px solid rgb(116,165,33);\n"
        "\n"
        "}")
                self.menu_btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.menu_btn.setFrameShadow(QtWidgets.QFrame.Raised)
                self.menu_btn.setObjectName("menu_btn")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu_btn)
                self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
                self.verticalLayout_2.setSpacing(5)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.btn = QtWidgets.QPushButton(self.menu_btn)
                self.btn.setStyleSheet("QPushButton#btn{\n"
        "    border:0px solid;\n"
        "}\n"
        "")
                self.btn.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/asset/cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                self.btn.setIcon(icon)
                self.btn.setIconSize(QtCore.QSize(50, 50))
                self.btn.setObjectName("btn")
                self.verticalLayout_2.addWidget(self.btn)
                self.horizontalLayout.addWidget(self.menu_btn)

                # judul pass manager
                self.label_passManager = QtWidgets.QFrame(self.topBar)
                self.label_passManager.setStyleSheet("background-color: rgb(17,25,39);")
                self.label_passManager.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.label_passManager.setFrameShadow(QtWidgets.QFrame.Raised)
                self.label_passManager.setObjectName("label_passManager")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.label_passManager)
                self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_3.setSpacing(0)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.title_passManager = QtWidgets.QLabel(self.label_passManager)
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.title_passManager.setFont(font)
                self.title_passManager.setStyleSheet("color: rgb(255, 255, 255);")
                self.title_passManager.setObjectName("title_passManager")

                # content page
                self.verticalLayout_3.addWidget(self.title_passManager)
                self.horizontalLayout.addWidget(self.label_passManager)
                self.verticalLayout.addWidget(self.topBar)
                self.content = QtWidgets.QFrame(self.centralwidget)
                self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.content.setFrameShadow(QtWidgets.QFrame.Raised)
                self.content.setObjectName("content")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.content)
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_2.setSpacing(0)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")

                # left menu
                self.left_menu = QtWidgets.QFrame(self.content)
                self.left_menu.setMinimumSize(QtCore.QSize(80, 0))
                self.left_menu.setMaximumSize(QtCore.QSize(80, 16777215))
                self.left_menu.setStyleSheet("background-color: rgb(17, 25, 39);")
                self.left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
                self.left_menu.setObjectName("left_menu")
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.left_menu)
                self.verticalLayout_4.setContentsMargins(0, 10, 0, 0)
                self.verticalLayout_4.setSpacing(0)
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.buton = QtWidgets.QFrame(self.left_menu)
                self.buton.setStyleSheet("")
                self.buton.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.buton.setFrameShadow(QtWidgets.QFrame.Raised)
                self.buton.setObjectName("buton")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.buton)
                self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout_5.setSpacing(10)

                # button add data
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.addData = QtWidgets.QPushButton(self.buton)
                self.addData.setMinimumSize(QtCore.QSize(0, 60))
                self.addData.setStyleSheet("QPushButton#addData{\n"
        "    border:0px solid;\n"
        "    color:white;\n"
        "}\n"
        "QPushButton#addData:hover{\n"
        "    border-bottom:4px solid rgb(116,165,33);\n"
        "}")
                self.addData.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap(":/asset/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                self.addData.setIcon(icon1)
                self.addData.setIconSize(QtCore.QSize(40, 50))
                self.addData.setObjectName("addData")
                self.verticalLayout_5.addWidget(self.addData)

                # button see credentials
                self.seeCreds = QtWidgets.QPushButton(self.buton)
                self.seeCreds.setMinimumSize(QtCore.QSize(0, 60))
                self.seeCreds.setStyleSheet("QPushButton#seeCreds{\n"
        "    border:0px solid;\n"
        "    color:white;\n"
        "}\n"
        "QPushButton#seeCreds:hover{\n"
        "    border-bottom:3px solid rgb(116,165,33);\n"
        "}")
                self.seeCreds.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap(":/asset/see.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                self.seeCreds.setIcon(icon2)
                self.seeCreds.setIconSize(QtCore.QSize(100, 50))
                self.seeCreds.setObjectName("seeCreds")
                self.verticalLayout_5.addWidget(self.seeCreds)
                self.frame_separator = QtWidgets.QFrame(self.buton)
                self.frame_separator.setStyleSheet("")
                self.frame_separator.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_separator.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_separator.setObjectName("frame_separator")
                self.verticalLayout_5.addWidget(self.frame_separator)

                # button log out
                self.logOut = QtWidgets.QPushButton(self.buton)
                self.logOut.setMinimumSize(QtCore.QSize(0, 60))
                self.logOut.setStyleSheet("QPushButton#logOut{\n"
        "    border:0px solid;\n"
        "    color:white;\n"
        "}\n"
        "QPushButton#logOut:hover{\n"
        "    border-bottom:4px solid rgb(116,165,33);\n"
        "}")
                self.logOut.setText("")
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap(":/asset/logOut.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                self.logOut.setIcon(icon3)
                self.logOut.setIconSize(QtCore.QSize(100, 50))
                self.logOut.setAutoDefault(False)
                self.logOut.setDefault(True)
                self.logOut.setFlat(True)
                self.logOut.setObjectName("logOut")
                self.verticalLayout_5.addWidget(self.logOut, 0, QtCore.Qt.AlignBottom)
                self.verticalLayout_4.addWidget(self.buton)
                self.horizontalLayout_2.addWidget(self.left_menu)

                # pages
                self.pages = QtWidgets.QFrame(self.content)
                self.pages.setStyleSheet("/*background-color: rgb(85, 255, 0);*/")
                self.pages.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.pages.setFrameShadow(QtWidgets.QFrame.Raised)
                self.pages.setObjectName("pages")
                self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.pages)
                self.verticalLayout_6.setObjectName("verticalLayout_6")
                self.stackedWidget = QtWidgets.QStackedWidget(self.pages)
                self.stackedWidget.setObjectName("stackedWidget")

                # pages add data
                self.add = QtWidgets.QWidget()
                self.add.setObjectName("add")
                self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.add)
                self.verticalLayout_7.setObjectName("verticalLayout_7")
                self.background_frame = QtWidgets.QFrame(self.add)
                self.background_frame.setMinimumSize(QtCore.QSize(10, 0))
                self.background_frame.setAutoFillBackground(False)
                self.background_frame.setStyleSheet("image: url(:/asset/key pass manager (fix).png);")
                self.background_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.background_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.background_frame.setObjectName("background_frame")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.background_frame)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.Input_data_frame = QtWidgets.QFrame(self.background_frame)
                self.Input_data_frame.setMinimumSize(QtCore.QSize(350, 0))
                self.Input_data_frame.setMaximumSize(QtCore.QSize(500, 16777215))
                self.Input_data_frame.setStyleSheet("image:none;")
                self.Input_data_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Input_data_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Input_data_frame.setObjectName("Input_data_frame")
                self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Input_data_frame)
                self.verticalLayout_9.setContentsMargins(20, 0, 0, 10)
                self.verticalLayout_9.setSpacing(25)
                self.verticalLayout_9.setObjectName("verticalLayout_9")
                self.title_new = QtWidgets.QLabel(self.Input_data_frame)
                self.title_new.setMinimumSize(QtCore.QSize(0, 50))
                self.title_new.setMaximumSize(QtCore.QSize(16777215, 50))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.title_new.setFont(font)
                self.title_new.setStyleSheet("color:white;\n"
        "image: none;\n"
        "")
                self.title_new.setScaledContents(True)
                self.title_new.setAlignment(QtCore.Qt.AlignCenter)
                self.title_new.setObjectName("title_new")
                self.verticalLayout_9.addWidget(self.title_new)

                # website field
                self.website_field = QtWidgets.QLineEdit(self.Input_data_frame)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.website_field.setFont(font)
                self.website_field.setStyleSheet("border:none;\n"
        "color:rgb(255,255,255);\n"
        "border-bottom: 2px solid rgb(255,255,255);\n"
        "padding-bottom:10px;\n"
        "image:none;")
                self.website_field.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.website_field.setObjectName("website_field")
                self.verticalLayout_9.addWidget(self.website_field)

                # email field
                self.email_field = QtWidgets.QLineEdit(self.Input_data_frame)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.email_field.setFont(font)
                self.email_field.setStyleSheet("border:none;\n"
        "color:rgb(255,255,255);\n"
        "border-bottom: 2px solid rgb(255,255,255);\n"
        "padding-bottom:10px;\n"
        "image:none;")
                self.email_field.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.email_field.setObjectName("email_field")
                self.verticalLayout_9.addWidget(self.email_field)

                # pass field
                self.pass_field = QtWidgets.QLineEdit(self.Input_data_frame)
                font = QtGui.QFont()
                font.setPointSize(9)
                self.pass_field.setFont(font)
                self.pass_field.setStyleSheet("border:none;\n"
        "color:rgb(255,255,255);\n"
        "border-bottom: 2px solid rgb(255,255,255);\n"
        "padding-bottom:10px;\n"
        "image:none;")
                self.pass_field.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.pass_field.setObjectName("pass_field")
                self.pass_field.setEchoMode(QtWidgets.QLineEdit.Password)
                self.verticalLayout_9.addWidget(self.pass_field)
                # submit btn
                self.submit = QtWidgets.QPushButton(self.Input_data_frame)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.submit.setFont(font)
                self.submit.setStyleSheet("QPushButton#submit{\n"
        "    background-color: rgb(17, 25, 39);\n"
        "    color:#73777B;\n"
        "    border:2px solid #73777B;\n"
        "}\n"
        "QPushButton#submit:hover{\n"
        "    color:white;\n"
        "}\n"
        "\n"
        "QPushButton#submit:pressed{\n"
        "    padding-top:3px;\n"
        "    padding-left:3px;\n"
        "}")
                self.submit.setObjectName("submit")
                self.verticalLayout_9.addWidget(self.submit)
                self.horizontalLayout_4.addWidget(self.Input_data_frame, 0, QtCore.Qt.AlignLeft)
                self.frame_2 = QtWidgets.QFrame(self.background_frame)
                self.frame_2.setMaximumSize(QtCore.QSize(200, 16777215))
                self.frame_2.setStyleSheet("image:none;")
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setObjectName("frame_2")
                self.horizontalLayout_4.addWidget(self.frame_2, 0, QtCore.Qt.AlignRight)
                self.verticalLayout_7.addWidget(self.background_frame)
                self.stackedWidget.addWidget(self.add)

                # page see credential
                self.see = QtWidgets.QWidget()
                self.see.setMinimumSize(QtCore.QSize(0, 0))
                self.see.setObjectName("see")
                self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.see)
                self.verticalLayout_8.setContentsMargins(-1, 25, -1, -1)
                self.verticalLayout_8.setObjectName("verticalLayout_8")
                self.title_see = QtWidgets.QLabel(self.see)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.title_see.setFont(font)
                self.title_see.setStyleSheet("color:white;")
                self.title_see.setAlignment(QtCore.Qt.AlignCenter)
                self.title_see.setObjectName("title_see")
                self.verticalLayout_8.addWidget(self.title_see)

                # table frame
                self.table_frame = QtWidgets.QFrame(self.see)
                self.table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.table_frame.setObjectName("table_frame")
                self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.table_frame)
                self.verticalLayout_10.setObjectName("verticalLayout_10")

                # table data
                self.table_data = QtWidgets.QTableWidget(self.table_frame)
                self.table_data.setMinimumSize(QtCore.QSize(1000, 500))
                self.table_data.setMaximumSize(QtCore.QSize(16777215, 500))
                self.table_data.setStyleSheet("border:1px solid black;\n""color:black;\n"
                "background-color:white;")
                self.table_data.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                self.table_data.setShowGrid(True)
                self.table_data.setObjectName("table_data")
                self.table_data.setColumnCount(5)
                item = QtWidgets.QTableWidgetItem()
                self.table_data.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.table_data.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.table_data.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.table_data.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.table_data.setHorizontalHeaderItem(4, item)
                self.table_data.horizontalHeader().setDefaultSectionSize(200)
                self.verticalLayout_10.addWidget(self.table_data)
                self.verticalLayout_8.addWidget(self.table_frame)
                self.btn_table = QtWidgets.QFrame(self.see)
                self.btn_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.btn_table.setFrameShadow(QtWidgets.QFrame.Raised)
                self.btn_table.setObjectName("btn_table")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.btn_table)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")

                # delete data button
                self.delete_data = QtWidgets.QPushButton(self.btn_table)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.delete_data.setFont(font)
                self.delete_data.setStyleSheet("QPushButton#delete_data{\n"
        "    background-color: rgb(17, 25, 39);\n"
        "    color:rgb(175,248,30);\n"
        "    border:2px solid rgb(175,248,30);\n"
        "}\n"
        "QPushButton#delete_data:hover{\n"
        "    color:white;\n"
        "}\n"
        "\n"
        "QPushButton#delete_data:pressed{\n"
        "    padding-left:3px;\n"
        "    padding-top:3px;\n"
        "}")
                self.delete_data.setObjectName("delete_data")
                self.horizontalLayout_3.addWidget(self.delete_data)

                # show pass button
                self.show_pass = QtWidgets.QPushButton(self.btn_table)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.show_pass.setFont(font)
                self.show_pass.setStyleSheet("QPushButton#show_pass{\n"
        "    background-color: rgb(17, 25, 39);\n"
        "    color:rgb(175,248,30);\n"
        "    border:2px solid rgb(175,248,30);\n"
        "}\n"
        "QPushButton#show_pass:hover{\n"
        "    color:white;\n"
        "}\n"
        "\n"
        "QPushButton#show_pass:pressed{\n"
        "    padding-left:3px;\n"
        "    padding-top:3px;\n"
        "}")
                self.show_pass.setObjectName("show_pass")
                self.horizontalLayout_3.addWidget(self.show_pass)

                # update data button
                self.update_data = QtWidgets.QPushButton(self.btn_table)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.update_data.setObjectName("update_data")
                self.update_data.setFont(font)
                self.update_data.setStyleSheet("QPushButton#update_data{\n"
        "	background-color: rgb(17, 25, 39);\n"
        "	color:rgb(175,248,30);\n"
        "	border:2px solid rgb(175,248,30);\n"
        "}\n"
        "QPushButton#update_data:hover{\n"
        "	color:white;\n"
        "}\n"
        "\n"
        "QPushButton#update_data:pressed{\n"
        "	padding-left:3px;\n"
        "	padding-top:3px;\n"
        "}")

                self.horizontalLayout_3.addWidget(self.update_data)

                # refresh table button
                self.refresh_table = QtWidgets.QPushButton(self.btn_table)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.refresh_table.setObjectName("refresh_table")
                self.refresh_table.setFont(font)
                self.refresh_table.setStyleSheet("QPushButton#refresh_table{\n"
        "	background-color: rgb(17, 25, 39);\n"
        "	color:rgb(175,248,30);\n"
        "	border:2px solid rgb(175,248,30);\n"
        "}\n"
        "QPushButton#refresh_table:hover{\n"
        "	color:white;\n"
        "}\n"
        "\n"
        "QPushButton#refresh_table:pressed{\n"
        "	padding-left:3px;\n"
        "	padding-top:3px;\n"
        "}")

                self.horizontalLayout_3.addWidget(self.refresh_table)

                # delete all button
                self.delete_all = QtWidgets.QPushButton(self.btn_table)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.delete_all.setFont(font)
                self.delete_all.setStyleSheet("QPushButton#delete_all{\n"
        "    background-color: red;\n"
        "    color:rgb(175,248,30);\n"
        "    border:2px solid white;\n"
        "}\n"
        "QPushButton#delete_all:hover{\n"
        "    color:white;\n"
        "}\n"
        "\n"
        "QPushButton#delete_all:pressed{\n"
        "    padding-left:3px;\n"
        "    padding-top:3px;\n"
        "}")
                self.delete_all.setObjectName("delete_all")
                self.horizontalLayout_3.addWidget(self.delete_all)
                self.verticalLayout_8.addWidget(self.btn_table)
                self.stackedWidget.addWidget(self.see)


                self.verticalLayout_6.addWidget(self.stackedWidget)
                self.horizontalLayout_2.addWidget(self.pages)
                self.verticalLayout.addWidget(self.content)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.stackedWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.title_passManager.setText(_translate("MainWindow", "      J A C K P A S S  M A N A G E R"))
                self.title_new.setText(_translate("MainWindow", "New Data"))
                self.website_field.setPlaceholderText(_translate("MainWindow", "  Website"))
                self.email_field.setPlaceholderText(_translate("MainWindow", "  Email"))
                self.pass_field.setPlaceholderText(_translate("MainWindow", "  Password"))
                self.submit.setText(_translate("MainWindow", "Submit"))
                self.title_see.setText(_translate("MainWindow", "Credential"))
                item = self.table_data.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID"))
                item = self.table_data.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Website"))
                item = self.table_data.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Email"))
                item = self.table_data.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "Password"))
                item = self.table_data.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "Time"))
                self.delete_data.setText(_translate("MainWindow", "Delete"))
                self.show_pass.setText(_translate("MainWindow", "Show Password"))
                self.update_data.setText(_translate("MainWindow","Update Data"))
                self.refresh_table.setText(_translate("MainWindow", "Refresh"))
                self.delete_all.setText(_translate("MainWindow", "Delete All Entries"))