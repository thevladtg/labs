#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        Метод для кнопки "Заполнить случайными числами"
        Случайные числа от 1 до 100
        """
        self.label_info.setText("")
        row = 0
        col = 0
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 100)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0

    def solve(self):
        count = 0
        max_value = -float('inf')
        max_row = -1
        max_col = -1
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                value = int(self.tableWidget.item(row, col).text())
                if value % 2 == 0:
                    count += 1
                if value > max_value:
                    max_value = value
                    max_row = row
                    max_col = col
                    break
        new_max_value = max_value + count
        self.tableWidget.setItem(max_row, max_col, QTableWidgetItem(str(new_max_value)))
        self.label_info.setText(f"Макс до : {max_value}, макс после : {new_max_value}")


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
