
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(643, 693)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, -10, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.list = QtWidgets.QListWidget(Dialog)
        self.list.setGeometry(QtCore.QRect(20, 250, 611, 411))
        self.list.setObjectName("list")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 230, 91, 16))
        self.label_2.setObjectName("label_2")
        self.delete_button = QtWidgets.QPushButton(Dialog, clicked = lambda: self.delete())
        self.delete_button.setGeometry(QtCore.QRect(550, 260, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(30, 60, 351, 41))
        self.name.setObjectName("name")
        self.date = QtWidgets.QLineEdit(Dialog)
        self.date.setGeometry(QtCore.QRect(450, 60, 141, 41))
        self.date.setObjectName("date")
        self.time = QtWidgets.QLineEdit(Dialog)
        self.time.setGeometry(QtCore.QRect(450, 120, 141, 41))
        self.time.setObjectName("time")
        self.theme = QtWidgets.QLineEdit(Dialog)
        self.theme.setGeometry(QtCore.QRect(30, 120, 351, 41))
        self.theme.setObjectName("theme")
        self.button1 = QtWidgets.QPushButton(Dialog, clicked = lambda: self.clicked())
        self.button1.setGeometry(QtCore.QRect(290, 220, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(450, 40, 131, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(450, 100, 131, 16))
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(50, 180, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 180, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(350, 180, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(500, 180, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "EVENT ORGANIZING SYSTEM"))
        self.label_2.setText(_translate("Dialog", "List of Events"))
        self.delete_button.setText(_translate("Dialog", "Delete"))
        self.button1.setText(_translate("Dialog", "Add Event"))
        self.label_3.setText(_translate("Dialog", "Name/s of the Celebrant"))
        self.label_4.setText(_translate("Dialog", "Theme"))
        self.label_5.setText(_translate("Dialog", "Date"))
        self.label_6.setText(_translate("Dialog", "Time"))
        self.radioButton.setText(_translate("Dialog", "Birthday"))
        self.radioButton_2.setText(_translate("Dialog", "Wedding"))
        self.radioButton_3.setText(_translate("Dialog", "Party"))
        self.radioButton_4.setText(_translate("Dialog", "Thanksgiving"))

        list = []
    def clicked(self):
        name = self.name.text()
        date = self.date.text()
        time = self.time.text()
        theme = self.theme.text()

        if self.radioButton.isChecked():
            self.list.addItem("Event: Birthday, Theme: " + theme + ", Name of the Celebrant: " + name + ", Date: " + date + ", Time: " + time) 
        elif self.radioButton_2.isChecked():
            self.list.addItem("Event: Wedding, Theme: " + theme + ", Name of the Celebrant: " + name + ", Date: " + date + ", Time: " + time) 
        elif self.radioButton_3.isChecked():
            self.list.addItem("Event: Party, Theme: " + theme + ", Name of the Celebrant: " + name + ", Date: " + date + ", Time: " + time) 
        elif self.radioButton_4.isChecked():
            self.list.addItem("Event: Thanksgiving, Theme: " + theme + ", Name of the Celebrant: " + name + ", Date: " + date + ", Time: " + time) 
    
    def delete(self):
        delete = self.list.currentRow()
        self.list.takeItem(delete)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
