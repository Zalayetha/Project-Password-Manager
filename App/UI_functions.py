from main import *
import db_connect
from db_connect import *

class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        print("berhasil")
        if enable:

            # width
            width = self.ui.left_menu.width()
            maxExtend = maxWidth
            standard = 80

            # max width
            if width == 80:
                widthExtended = maxExtend
                self.ui.addData.setText("A D D  D A T A")
                self.ui.seeCreds.setText("C R E D E N T I A L") 
                self.ui.logOut.setText("E X I T") 
            else:
                widthExtended = standard
                self.ui.addData.setText("")
                self.ui.seeCreds.setText("")
                self.ui.logOut.setText("")

            # animation
            self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
    
    def removed_field(website,email,password):
        website.clear()
        email.clear()
        password.clear()

    def input_data(self):
        self.ui.table_data.setRowCount(len(db_connect.result))
        table_row = 0
        for row in db_connect.result:
            self.ui.table_data.setItem(table_row,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.table_data.setItem(table_row,1,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.table_data.setItem(table_row,2,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.table_data.setItem(table_row,3,QtWidgets.QTableWidgetItem('*'*len(decrypt(row[3]))))
            self.ui.table_data.setItem(table_row,4,QtWidgets.QTableWidgetItem(row[4]))
            table_row+=1
    
    def disable_btn(self):
        if len(self.ui.website_field.text())>0 and len(self.ui.email_field.text())>0 and len(self.ui.pass_field.text())>0:
            self.ui.submit.setDisabled(False)
            self.ui.submit.setStyleSheet("QPushButton#submit{\n"
            "    background-color: rgb(17, 25, 39);\n"
            "    color:rgb(175,248,30);\n"
            "    border:2px solid rgb(175,248,30);\n"
            "}\n"
            "QPushButton#submit:hover{\n"
            "    color:white;\n"
            "}\n"
            "\n"
            "QPushButton#submit:pressed{\n"
            "    padding-top:3px;\n"
            "    padding-left:3px;\n"
            "}")

               
        else:
            self.ui.submit.setDisabled(True)
            self.ui.submit.setStyleSheet("QPushButton#submit{\n"
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
    
    def clear_row(self):
            self.confirm_del = QMessageBox.question(None,'Warning','Are you sure you want to delete the data',QMessageBox.Yes|QMessageBox.No)
            if self.confirm_del == QMessageBox.Yes:
                try:
                    for item in self.ui.table_data.selectedItems():
                        id=item.text()
                
                    delete_row(int(id))
                    self.ui.table_data.removeRow(self.ui.table_data.currentRow())
                except Exception: 
                    self.error = QMessageBox()
                    self.error.setWindowTitle("Warning")
                    self.error.setText("You Must Click The ID !")
                    self.error.setIcon(QMessageBox.Warning)
                    self.error.setStandardButtons(QMessageBox.Ok)
                    self.error.exec_()
      
       

    def msgBox_show_pass(self):
        try:
            for item in self.ui.table_data.selectedItems():
                id=item.text()
            show_pass(int(id))
            self.showPass = QMessageBox()
            self.showPass.setWindowTitle("Information")
            self.showPass.setText("Your Password is ")
            self.showPass.setIcon(QMessageBox.Information)
            self.showPass.setStandardButtons(QMessageBox.Ok)
            for item in db_connect.result:
                self.showPass.setInformativeText(decrypt(item[0])) 
            self.showPass.exec_()
        except Exception:
            self.showPass = QMessageBox()
            self.showPass.setWindowTitle("Warning")
            self.showPass.setText("You Must Click The ID !")
            self.showPass.setIcon(QMessageBox.Warning)
            self.showPass.setStandardButtons(QMessageBox.Ok)
            self.showPass.exec_()
    
    def clear_all(self):
        try:
            self.confirm_del = QMessageBox.question(None,'Warning','Are you sure you want to delete all the data',QMessageBox.Yes|QMessageBox.No)
            if self.confirm_del == QMessageBox.Yes:
                delete_all_entries()
                self.ui.table_data.setRowCount(0)
        except Exception as err:
            print(err)


    def succeed_store(self):
        try:
            db_connect.store_pass(self.ui.website_field.text(),self.ui.email_field.text(),self.ui.pass_field.text(),self.current_time)
            self.succed = QMessageBox() 
            self.succed.setWindowTitle("Store Password")
            self.succed.setText("Succeed !")
            self.succed.setIcon(QMessageBox.Information)
            self.succed.setStandardButtons(QMessageBox.Ok)
            self.succed.exec_()
        except sqlite3.Error:
            self.failed = QMessageBox() 
            self.failed.setWindowTitle("Store Password")
            self.failed.setText("Failed !")
            self.failed.setIcon(QMessageBox.Critical)
            self.failed.setStandardButtons(QMessageBox.Ok)
            self.failed.exec_()
    
    def switch_window(self,username,password):
        validation = db_connect.login_validation(username,password)
        try:
            if validation:
                self.dashboard()
                self.Form.hide()
            else:
                pass
        except Exception as err:
            print(err)
    
    def exit(self):
        sys.exit()