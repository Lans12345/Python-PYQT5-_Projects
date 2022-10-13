
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(636, 414)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 0, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listHalf = QtWidgets.QListWidget(Dialog)
        self.listHalf.setGeometry(QtCore.QRect(30, 170, 271, 221))
        self.listHalf.setObjectName("listHalf")
        self.listFully = QtWidgets.QListWidget(Dialog)
        self.listFully.setGeometry(QtCore.QRect(330, 170, 281, 221))
        self.listFully.setObjectName("listFully")
        self.half = QtWidgets.QLineEdit(Dialog)
        self.half.setGeometry(QtCore.QRect(60, 80, 211, 31))
        self.half.setText("")
        self.half.setFrame(True)
        self.half.setObjectName("half")
        self.b1 = QtWidgets.QPushButton(Dialog, clicked = lambda: self.clicked())
        self.b1.setGeometry(QtCore.QRect(130, 130, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.fully = QtWidgets.QLineEdit(Dialog)
        self.fully.setGeometry(QtCore.QRect(360, 80, 211, 31))
        self.fully.setObjectName("fully")
        self.b2 = QtWidgets.QPushButton(Dialog, clicked = lambda: self.clicked1())
        self.b2.setGeometry(QtCore.QRect(430, 130, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(360, 60, 131, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Vaccine Monitoring"))
        self.b1.setText(_translate("Dialog", "Enter"))
        self.b2.setText(_translate("Dialog", "Enter"))
        self.label_2.setText(_translate("Dialog", "Name for Half Vaccinated"))
        self.label_3.setText(_translate("Dialog", "Name for Fully Vaccinated"))

    def clicked(self):
        name = self.half.text()
        self.listHalf.addItem(name)
        self.half.setText("")

    def clicked1(self):
        name1 = self.fully.text()
        self.listFully.addItem(name1)
        self.fully.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
