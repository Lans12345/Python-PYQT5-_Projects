

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 399)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.task = QtWidgets.QLineEdit(Dialog)
        self.task.setGeometry(QtCore.QRect(60, 90, 351, 41))
        self.task.setObjectName("task")
        self.button = QtWidgets.QPushButton(Dialog, clicked = lambda: self.clicked())
        self.button.setGeometry(QtCore.QRect(440, 100, 111, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.list = QtWidgets.QListWidget(Dialog)
        self.list.setGeometry(QtCore.QRect(60, 150, 481, 221))
        self.list.setObjectName("list")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.delete())
        self.pushButton.setGeometry(QtCore.QRect(450, 340, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "To - Do List"))
        self.label.setText(_translate("Dialog", "To - Do List"))
        self.button.setText(_translate("Dialog", "Add Task"))
        self.label_2.setText(_translate("Dialog", "Enter Task"))
        self.pushButton.setText(_translate("Dialog", "Delete"))

    def clicked(self):
        task = self.task.text()
        self.list.addItem(task)
        self.task.setText("")

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
