import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
import sqlite3


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main2.ui', self)
        self.push.clicked.connect(self.window)
        data = sqlite3.connect('coffee.db')

        cur = data.cursor()
        result = cur.execute("SELECT * FROM Coffee").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(['id', 'Название', 'Степень прожарки', 'Тип', 'Вкус', 'Цена',
                                                    'Объём'])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def window(self):
        self.wind = Redact()
        self.wind.show()


class Redact(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.data = sqlite3.connect('coffee.db')
        self.cur = self.data.cursor()
        self.push1.clicked.connect(self.adding)
        self.push2.clicked.connect(self.editing)
        self.modified = {}
        self.titles = None

    def adding(self):
        self.id = self.id.text()
        self.n = self.name.text()
        self.r = self.roast.text()
        self.mz = self.const_2.text()
        self.t = self.taste.text()
        self.p = self.price.text()
        self.v = self.volume.text()
        self.add = """INSERT into Coffee(name, roasting, type, taste, price, volume)
                                               VALUES(?, ?, ?, ?, ?, ?)"""

        self.tuple = (self.n, self.r, self.mz, self.t, self.p, self.v)
        self.cur.execute(self.add, self.tuple)
        self.data.commit()

        msg_sn = QMessageBox()  # показываем небольшое окошко, в котором сообщаем, что сохранение данных о номинанте
        msg_sn.setWindowTitle("Поздравляем!")  # прошло успешно
        msg_sn.setText("Вы успешно добавили в БД новый товар")
        msg_sn.setIcon(QMessageBox.Information)
        msg_sn.exec_()

    def editing(self):
        self.id = self.id.text()
        self.n = self.name.text()
        self.r = self.roast.text()
        self.mz = self.const_2.text()
        self.t = self.taste.text()
        self.p = self.price.text()
        self.v = self.volume.text()
        print(self.id)
        if self.n:
            self.result = self.cur.execute('''UPDATE Coffee
            SET name=?
            WHERE id=?''', (self.n, self.id))
            self.data.commit()
        if self.r:
           self.result = self.cur.execute('''UPDATE Coffee
                        SET roasting=?
                        WHERE id=?''', (self.r, self.id))
           self.data.commit()
        if self.mz:
           self.result = self.cur.execute('''UPDATE Coffee
                        SET type=?
                        WHERE id=?''', (self.mz, self.id))
           self.data.commit()
        if self.t:
           self.result = self.cur.execute('''UPDATE Coffee
                        SET taste=?
                        WHERE id=?''', (self.t, self.id))
           self.data.commit()
        if self.p:
           self.result = self.cur.execute('''UPDATE Coffee
                        SET price=?
                        WHERE id=?''', (self.p, self.id))
           self.data.commit()
        if self.v:
            self.result = self.cur.execute('''UPDATE Coffee
                                   SET volume=?
                                   WHERE id=?''', (self.v, self.id))
            self.data.commit()
        self.data.commit()
        msg_sn = QMessageBox()  # показываем небольшое окошко, в котором сообщаем, что сохранение данных о номинанте
        msg_sn.setWindowTitle("Поздравляем!")  # прошло успешно
        msg_sn.setText("Вы изменили данные о товаре")
        msg_sn.setIcon(QMessageBox.Information)
        msg_sn.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cf = Coffee()
    cf.show()
    sys.exit(app.exec())
