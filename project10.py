
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(672, 482)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 0, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.list = QtWidgets.QListWidget(Dialog)
        self.list.setGeometry(QtCore.QRect(10, 60, 411, 401))
        self.list.setObjectName("list")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 81, 16))
        self.label_2.setObjectName("label_2")
        self.button2 = QtWidgets.QPushButton(Dialog, clicked = lambda: self.delete_button())
        self.button2.setGeometry(QtCore.QRect(330, 70, 75, 23))
        self.button2.setObjectName("button2")
        self.title = QtWidgets.QLineEdit(Dialog)
        self.title.setGeometry(QtCore.QRect(440, 70, 221, 41))
        self.title.setObjectName("title")
        self.author = QtWidgets.QLineEdit(Dialog)
        self.author.setGeometry(QtCore.QRect(440, 160, 221, 41))
        self.author.setObjectName("author")
        self.date = QtWidgets.QLineEdit(Dialog)
        self.date.setGeometry(QtCore.QRect(520, 250, 141, 41))
        self.date.setObjectName("date")
        self.button1 = QtWidgets.QPushButton(Dialog, clicked = lambda: self.clicked())
        self.button1.setGeometry(QtCore.QRect(520, 350, 75, 23))
        self.button1.setObjectName("button1")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(440, 50, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(440, 140, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(520, 230, 91, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Book Listing Program"))
        self.label_2.setText(_translate("Dialog", "List of Books"))
        self.button2.setText(_translate("Dialog", "Delete"))
        self.button1.setText(_translate("Dialog", "Add"))
        self.label_3.setText(_translate("Dialog", "Title of the Book"))
        self.label_4.setText(_translate("Dialog", "Author"))
        self.label_5.setText(_translate("Dialog", "Date Published"))

        list = []

    def clicked(self):
        title = self.title.text()
        author = self.author.text()
        date = self.date.text()

        self.list.addItem("Title: " + title + ", Author: " + author + ", Date Published: " + date)

        self.title.setText("")
        self.author.setText("")
        self.date.setText("")

    def delete_button(self):
        remove = self.list.currentRow()
        self.list.takeItem(remove)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
