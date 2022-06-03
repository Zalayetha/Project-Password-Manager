from PyQt5 import  QtGui, QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5.QtCore import QPropertyAnimation
import time
import sys

# GUI FILE
from app import Ui_MainWindow
from login import Ui_Form

# UI FUNCTIONS FILE
from UI_functions import *


# db_connect File
import db_connect
from db_connect import *


# Manage Encrypt and decrypt function file
from manage import *

# resource
import resource

class MainWindow(QMainWindow):
     def __init__(self):
          self.app = QtWidgets.QApplication(sys.argv)
          self.Form = QtWidgets.QWidget()
          self.ui_login = Ui_Form()
          self.ui_login.setupUi(self.Form)
          self.Form.show()
          self.ui_login.Login.clicked.connect(lambda:UIFunctions.switch_window(self,self.ui_login.inputUser.text(),self.ui_login.inputPass.text()))
     
     def dashboard(self):
          db_connect.connect()
          QMainWindow.__init__(self)
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)
          self.setWindowTitle("JackPass Manager")
          self.setWindowIcon(QtGui.QIcon(":/asset/key pass manager (fix).png"))
          self.current_time = time.strftime('%I:%M %p, %d-%m-%Y')
          self.show()

          # Expand Menu
          self.ui.btn.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

          # New Data Page
          self.ui.addData.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.add))

          # See Credentials Page
          self.ui.seeCreds.clicked.connect(lambda:find_plainpass())
          self.ui.seeCreds.clicked.connect(lambda:UIFunctions.input_data(self))
          self.ui.seeCreds.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.see))
          

          # Submit Button
          self.ui.submit.setDisabled(True)
          self.ui.website_field.textChanged.connect(lambda:UIFunctions.disable_btn(self))
          self.ui.email_field.textChanged.connect(lambda:UIFunctions.disable_btn(self))
          self.ui.pass_field.textChanged.connect(lambda:UIFunctions.disable_btn(self))
          self.ui.submit.clicked.connect(lambda:UIFunctions.succeed_store(self))
          self.ui.submit.clicked.connect(lambda:UIFunctions.removed_field(self.ui.website_field,self.ui.email_field,self.ui.pass_field))
          
          

          # show password button
          self.ui.show_pass.clicked.connect(lambda:UIFunctions.msgBox_show_pass(self))

          # delete data button
          self.ui.delete_data.clicked.connect(lambda:UIFunctions.clear_row(self))

          # delete all entries button 
          self.ui.delete_all.clicked.connect(lambda:UIFunctions.clear_all(self))

          # logout button
          self.ui.logOut.clicked.connect(lambda:UIFunctions.exit(self))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())