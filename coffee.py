import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cf = Coffee()
    cf.show()
    sys.exit(app.exec())



