#!/usr/bin/env python3
# coding=utf-8

import re
import sys
import random
import string
#импортирую библиотеку для удобной работы со значениями
from collections import Counter
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_d.clicked.connect(self.deshef)

    def solve(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText()  # получаем наш текст
        # Разбиваем текст на слова
        words = text.split()
        # Обрабатываем каждое слово: удаляем второй символ
        processed_words = [word[:1] + word[2:] for word in words]
        # Объединяем обработанные слова в одну строку
        processed_text = ' '.join(processed_words)





        self.textEdit_words.setPlainText(processed_text)

    def deshef(self):
        # Получаем текущий текст
        text = self.textEdit_words.toPlainText()
        # Разбиваем текст на слова
        words = text.split()
        # Обрабатываем каждое слово: добавляем второй символ (рандомную букву)
        processed_words = [word[:1] + random.choice(string.ascii_letters) + word[1:] for word in words]
        # Объединяем обработанные слова в одну строку
        processed_text = ' '.join(processed_words)

        # Устанавливаем результат в виджет textEdit_text
        self.textEdit_text.clear()
        self.textEdit_text.setPlainText(processed_text)


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
