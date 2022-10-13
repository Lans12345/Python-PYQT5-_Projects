
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(425, 342)
        self.line = QtWidgets.QLineEdit(Dialog)
        self.line.setGeometry(QtCore.QRect(30, 30, 271, 31))
        self.line.setObjectName("line")
        self.button = QtWidgets.QPushButton(Dialog, clicked = lambda: self.clicked())
        self.button.setGeometry(QtCore.QRect(320, 40, 75, 23))
        self.button.setObjectName("button")
        self.list = QtWidgets.QListWidget(Dialog)
        self.list.setGeometry(QtCore.QRect(30, 80, 371, 251))
        self.list.setObjectName("list")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button.setText(_translate("Dialog", "Enter"))

    def clicked(self):
        student = self.line.text()
        self.list.addItem(student)
        self.line.setText("")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
