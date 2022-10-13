
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(609, 646)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(60, 90, 261, 41))
        self.name.setObjectName("name")
        self.qty = QtWidgets.QLineEdit(Dialog)
        self.qty.setGeometry(QtCore.QRect(370, 90, 141, 41))
        self.qty.setObjectName("qty")
        self.button = QtWidgets.QPushButton(Dialog, clicked = lambda: self.clicked())
        self.button.setGeometry(QtCore.QRect(260, 240, 75, 23))
        self.button.setObjectName("button")
        self.list = QtWidgets.QListWidget(Dialog)
        self.list.setGeometry(QtCore.QRect(20, 280, 571, 341))
        self.list.setObjectName("list")
        self.date = QtWidgets.QLineEdit(Dialog)
        self.date.setGeometry(QtCore.QRect(110, 180, 391, 41))
        self.date.setObjectName("date")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(370, 70, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 160, 161, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Inventory"))
        self.label.setText(_translate("Dialog", "Inventory"))
        self.button.setText(_translate("Dialog", "Enter"))
        self.label_2.setText(_translate("Dialog", "Name and Type of the Product"))
        self.label_3.setText(_translate("Dialog", "Quantity"))
        self.label_4.setText(_translate("Dialog", "Date"))

    def clicked(self):
        name = self.name.text()
        date = self.date.text()
        pcs = self.qty.text()

        self.list.addItem("Product: " + name + " Quantity: " + pcs + " Date Stored: " + date)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
