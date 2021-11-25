from PyQt5 import QtCore, QtWidgets
import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 60, 551, 321))
        self.table.setObjectName("table")
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        self.table.horizontalHeader().setDefaultSectionSize(78)
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.add.setObjectName("add")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "title"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "degree"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "type"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "description"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "price"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "volume"))
        self.add.setText(_translate("MainWindow", "добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "изменить"))


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 317)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 261, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(11)
        self.formLayout.setObjectName("formLayout")
        self.title = QtWidgets.QLabel(self.formLayoutWidget)
        self.title.setObjectName("title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.title)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.degree = QtWidgets.QLabel(self.formLayoutWidget)
        self.degree.setObjectName("degree")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.degree)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.type = QtWidgets.QLabel(self.formLayoutWidget)
        self.type.setObjectName("type")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.type)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.description = QtWidgets.QLabel(self.formLayoutWidget)
        self.description.setObjectName("description")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.description)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.price = QtWidgets.QLabel(self.formLayoutWidget)
        self.price.setObjectName("price")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.price)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.volume = QtWidgets.QLabel(self.formLayoutWidget)
        self.volume.setObjectName("volume")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.volume)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 220, 47, 13))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 240, 101, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "title"))
        self.degree.setText(_translate("MainWindow", "degree"))
        self.type.setText(_translate("MainWindow", "type"))
        self.comboBox.setItemText(0, _translate("MainWindow", "молотый"))
        self.comboBox.setItemText(1, _translate("MainWindow", "в зёрнах"))
        self.description.setText(_translate("MainWindow", "description"))
        self.price.setText(_translate("MainWindow", "price"))
        self.volume.setText(_translate("MainWindow", "volume"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "добавить запись"))


names = ['ID', 'title', 'degree', 'type', 'description', 'price', 'volume']


def view(other):
    other.table.clear()
    other.table.setRowCount(0)
    con = sqlite3.connect('../data/coffee.sqlite')
    cur = con.cursor()
    result = list(cur.execute(f"""SELECT * FROM info""").fetchall())
    con.close()
    other.table.setColumnCount(7)
    for i in range(7):
        other.table.setHorizontalHeaderItem(i, QTableWidgetItem(names[i]))
    for i, row in enumerate(result):
        other.table.setRowCount(other.table.rowCount() + 1)
        for j, elem in enumerate(row):
            if j == 3:
                elem = 'молотый' if int(elem) == 1 else 'в зёрнах'
            item = QTableWidgetItem(str(elem))
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            other.table.setItem(i, j, item)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        view(self)
        self.add.clicked.connect(self.click)
        self.pushButton_2.clicked.connect(self.click)

    def click(self):
        if self.sender().text() == 'добавить':
            self.second_form = Dialog(self, self.sender().text())
        else:
            if not self.table.item(self.table.currentRow(), 0) is None:
                a = self.table.item(self.table.currentRow(), 0).text()
                b = []
                for elem in [1, 2, 4, 5, 6, 3]:
                    b.append(self.table.item(self.table.currentRow(), elem).text())
                self.second_form = Dialog(self, self.sender().text(), args=b, id=a)
        self.second_form.show()

    def view(self):
        con = sqlite3.connect('../data/coffee.sqlite')
        cur = con.cursor()
        result = list(cur.execute(f"""SELECT * FROM info""").fetchall())
        con.close()
        self.table.setColumnCount(7)
        for i in range(7):
            self.table.setHorizontalHeaderItem(i, QTableWidgetItem(self.names[i]))
        for i, row in enumerate(result):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                item = QTableWidgetItem(str(elem))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.table.setItem(i, j, item)


class Dialog(QMainWindow, Ui_MainWindow2):
    def __init__(self, other, send, args=None, id=None):
        super().__init__()
        self.setupUi(self)
        self.label.hide()
        self.other, self.send, self.id = other, send, id
        self.label.resize(300, 20)
        self.pushButton.clicked.connect(self.click)
        if self.send == 'изменить':
            self.pushButton.setText('изменить запись')
            elems = [self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5, self.lineEdit_6]
            for i in range(len(elems)):
                elems[i].setText(args[i])
            args[-1] = 1 if args[-1] == 'молотый' else 2
            self.comboBox.setCurrentIndex(int(args[-1]) - 1)

    def click(self):
        b, c, = self.lineEdit_2.text(), self.lineEdit_3.text()
        d, e, f = self.comboBox.currentText(), self.lineEdit_4.text(), self.lineEdit_5.text()
        g = self.lineEdit_6.text()
        if b and c and d and e and f and g:
            if not f.isdigit():
                self.label.show()
                self.label.move(40, 215)
                self.label.setText('цена может быть только целым числом')
                return None
            if not g.isdigit():
                self.label.show()
                self.label.move(40, 215)
                self.label.setText('объём может быть только целым числом')
                return None
            else:
                d = 1 if d == 'молотый' else 2
                con = sqlite3.connect('../data/coffee.sqlite')
                cur = con.cursor()
                if self.send == 'добавить':
                    a = 'INSERT INTO info(title, degree, type, description, price, volume)'
                    cur.execute(f"""{a} VALUES("{b}", "{c}", {d}, "{e}", {f}, {g})""")
                else:
                    cur.execute(f"""
UPDATE info
SET title = "{b}"
WHERE id = {self.id}
""")
                    cur.execute(f"""
UPDATE info
SET degree = "{c}"
WHERE id = {self.id}
""")
                    cur.execute(f"""
UPDATE info
SET type = {d}
WHERE id = {self.id}
""")
                    cur.execute(f"""
UPDATE info
SET description = "{e}"
WHERE id = {self.id}
""")
                    cur.execute(f"""
UPDATE info
SET price = {f}
WHERE id = {self.id}
""")
                    cur.execute(f"""
UPDATE info
SET volume = {g}
WHERE id = {self.id}
""")
                con.commit()
                con.close()
                view(self.other)
                self.close()
        else:
            self.label.show()
            self.label.move(90, 215)
            self.label.setText('заполните все поля')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
