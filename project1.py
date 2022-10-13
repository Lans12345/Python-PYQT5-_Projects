
# Lance Olana - CpE 2B
# "Enrollment System"

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(641, 464)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 601, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 30, 121, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(430, 60, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(430, 100, 47, 13))
        self.label_4.setObjectName("label_4")
        self.lineName = QtWidgets.QLineEdit(self.tab)
        self.lineName.setGeometry(QtCore.QRect(80, 29, 331, 51))
        self.lineName.setObjectName("lineName")
        self.lineAddress = QtWidgets.QLineEdit(self.tab)
        self.lineAddress.setGeometry(QtCore.QRect(90, 100, 321, 71))
        self.lineAddress.setObjectName("lineAddress")
        self.lineSex = QtWidgets.QLineEdit(self.tab)
        self.lineSex.setGeometry(QtCore.QRect(460, 49, 113, 31))
        self.lineSex.setObjectName("lineSex")
        self.lineAge = QtWidgets.QLineEdit(self.tab)
        self.lineAge.setGeometry(QtCore.QRect(460, 100, 113, 31))
        self.lineAge.setObjectName("lineAge")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(110, 240, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(250, 240, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_3.setGeometry(QtCore.QRect(390, 240, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_4.setGeometry(QtCore.QRect(110, 280, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_5.setGeometry(QtCore.QRect(250, 280, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_6.setGeometry(QtCore.QRect(390, 280, 82, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.button1 = QtWidgets.QPushButton(self.tab, clicked = lambda: self.clicked())
        self.button1.setGeometry(QtCore.QRect(270, 330, 75, 23))
        self.button1.setObjectName("button1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.list = QtWidgets.QListWidget(self.tab_2)
        self.list.setGeometry(QtCore.QRect(20, 20, 561, 331))
        self.list.setObjectName("list")
        self.deleteButton = QtWidgets.QPushButton(self.tab_2, clicked = lambda: self.delete_Button())
        self.deleteButton.setGeometry(QtCore.QRect(480, 360, 75, 23))
        self.deleteButton.setObjectName("deleteButton")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def clicked(self):
        name = self.lineName.text()
        address = self.lineAddress.text()
        sex = self.lineSex.text()
        age = self.lineAge.text()
        
        if self.radioButton.isChecked():
            self.list.addItem(name  + ", " + age + ", " + sex + ", " + self.radioButton.text())
        elif self.radioButton_2.isChecked():
            self.list.addItem(name + ", " + age + ", " + sex + ", " + self.radioButton_2.text())
        elif self.radioButton_3.isChecked():
            self.list.addItem(name + ", " + age + ", " + sex + ", " + self.radioButton_3.text())
        elif self.radioButton_4.isChecked():
            self.list.addItem(name + ", " + age + ", " + sex + ", " + self.radioButton_4.text())
        elif self.radioButton_5.isChecked():
            self.list.addItem(name + ", " + age + ", " + sex + ", " + self.radioButton_5.text())
        elif self.radioButton_6.isChecked():
            self.list.addItem(name + ", " + age + ", " + sex + ", " + self.radioButton_6.text())
        
        

        self.lineAddress.setText("")
        self.lineName.setText("")
        self.lineSex.setText("")
        self.lineAge.setText("")
        
    def delete_Button(self):
        toDelete = self.list.currentRow()
        self.list.takeItem(toDelete)
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Enrollment"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.label_2.setText(_translate("Dialog", "Address:"))
        self.label_3.setText(_translate("Dialog", "Sex:"))
        self.label_4.setText(_translate("Dialog", "Age:"))
        self.radioButton.setText(_translate("Dialog", "Grade 7"))
        self.radioButton_2.setText(_translate("Dialog", "Grade 8"))
        self.radioButton_3.setText(_translate("Dialog", "Grade 9"))
        self.radioButton_4.setText(_translate("Dialog", "Grade 10"))
        self.radioButton_5.setText(_translate("Dialog", "Grade 11"))
        self.radioButton_6.setText(_translate("Dialog", "Grade 12"))
        self.button1.setText(_translate("Dialog", "Enroll"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Enrollment Tab"))
        self.deleteButton.setText(_translate("Dialog", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "List of Enrolled Student"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
