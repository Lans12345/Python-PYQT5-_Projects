
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(633, 493)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 0, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.list = QtWidgets.QListWidget(Dialog)
        self.list.setGeometry(QtCore.QRect(50, 210, 541, 261))
        self.list.setObjectName("list")
        self.model = QtWidgets.QLineEdit(Dialog)
        self.model.setGeometry(QtCore.QRect(60, 60, 311, 41))
        self.model.setObjectName("model")
        self.date = QtWidgets.QLineEdit(Dialog)
        self.date.setGeometry(QtCore.QRect(400, 60, 151, 41))
        self.date.setObjectName("date")
        self.brand = QtWidgets.QLineEdit(Dialog)
        self.brand.setGeometry(QtCore.QRect(200, 130, 221, 41))
        self.brand.setObjectName("brand")
        self.b1 = QtWidgets.QPushButton(Dialog, clicked = lambda: self.clicked())
        self.b1.setGeometry(QtCore.QRect(280, 180, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 110, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 40, 111, 16))
        self.label_4.setObjectName("label_4")
        self.sold = QtWidgets.QPushButton(Dialog, clicked = lambda: self.delete())
        self.sold.setGeometry(QtCore.QRect(500, 220, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sold.setFont(font)
        self.sold.setObjectName("sold")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Car Dealership"))
        self.label.setText(_translate("Dialog", "Car Dealership"))
        self.b1.setText(_translate("Dialog", "Enter"))
        self.label_2.setText(_translate("Dialog", "Model of the Car"))
        self.label_3.setText(_translate("Dialog", "Brand"))
        self.label_4.setText(_translate("Dialog", "Date of  the Model"))
        self.sold.setText(_translate("Dialog", "Sold"))

    def clicked(self):
        model = self.model.text()
        date = self.date.text()
        brand = self.brand.text()

        self.list.addItem("Model: " + model + " - Brand: " + brand + " - Date of the Model: " + date)
        self.model.setText("")
        self.date.setText("")
        self.brand.setText("")

    def delete(self):
        toDelete = self.list.currentRow()
        self.list.takeItem(toDelete)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
