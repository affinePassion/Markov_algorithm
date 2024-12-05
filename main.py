import sys
from typing import List
from markov import AlgorithmMarkov
from rules import Rules
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QInputDialog, QGraphicsRectItem)
from MainForm import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_num2.hide()
        self.ui.num2.hide()
        self.ui.label_plus.hide()
        self.ui.zameni_text.hide()
        self.ui.zameni_label.hide()
        self.ui.addButton.hide()
        self.ui.removeButton.hide()
        self.ui.left_zamena.hide()
        self.ui.right_zamena.hide()
        self.ui.label_arrow.hide()
        self.ui.buttonResult.clicked.connect(lambda: self.button_result_nums())
        self.ui.buttonResultString.clicked.connect(lambda: self.button_result_strings())
        self.ui.comboBox.currentTextChanged.connect(self.changeCombo)
        self.ui.comboBox_strings.currentTextChanged.connect(self.changeCombo)
        self.ui.addButton.clicked.connect(lambda: self.button_add_rule())
        self.ui.removeButton.clicked.connect(lambda: self.button_remove_rule())
        self._newRule = []
    
    def button_result_nums(self):
        if self.ui.comboBox.currentText()[0] == "1":
            msg = QMessageBox()
            num1 = self.ui.num1.text()
            try:
                int(num1)
            except:
                msg.setWindowTitle("Ошибка")
                msg.setText("Должно быть введено натуральное число")
                msg.exec_()
            if int(num1) <= 0:
                msg.setWindowTitle("Ошибка")
                msg.setText("Должно быть введено натуральное число")
                msg.exec_()
            else:
                rule = Rules()
                alg1 = AlgorithmMarkov(word = num1, rules = rule.rules_for_digits(1))
                self.ui.textEdit.setText(alg1.run())
                self.ui.result.setText(str(alg1.get_num()))
                print(f"Исходное число: {num1}\nПолученный результат: {self.ui.result.text()}")
                print(f"Работа алгоритма: {self.ui.textEdit.toPlainText()}")
        
        if self.ui.comboBox.currentText()[0] == "2":
            num1 = self.ui.num1.text()
            try:
                int(num1)
            except:
                msg.setWindowTitle("Ошибка")
                msg.setText("Должно быть введено натуральное число")
                msg.exec_()
            if int(num1) <= 0:
                msg.setWindowTitle("Ошибка")
                msg.setText("Должно быть введено натуральное число")
                msg.exec_()
            else:
                rule = Rules()
                alg1 = AlgorithmMarkov(word = num1, rules = rule.rules_for_digits(2))
                self.ui.textEdit.setText(alg1.run())
                self.ui.result.setText(str(alg1.get_num()))
                print(f"Исходное число: {num1}\nПолученный результат: {self.ui.result.text()}")
                print(f"Работа алгоритма: {self.ui.textEdit.toPlainText()}")

        if self.ui.comboBox.currentText()[0] == "3":
            num1 = self.ui.num1.text()
            num2 = self.ui.num2.text()
            try:
                int(num1)
                int(num2)
            except:
                msg.setWindowTitle("Ошибка")
                msg.setText("Должно быть введено натуральное число")
                msg.exec_()
            if int(num1) <= 0 or int(num2) <=0:
                msg.setWindowTitle("Ошибка")
                msg.setText("Должно быть введено натуральное число")
                msg.exec_()
            else:
                rule = Rules()
                alg1 = AlgorithmMarkov(word = num1, rules = rule.rules_for_digits(2))
                alg2 = AlgorithmMarkov(word = num2, rules = rule.rules_for_digits(1))
                stringOfPermutationsPlus = ""
                stringOfPermutationsMinus = ""
                while alg1.get_num() > 0:
                    stringOfPermutationsMinus += alg1.run() + "\n"
                    stringOfPermutationsPlus += alg2.run() + "\n"
                
                stringOfPermutationsMinus += "------------------------------------\n" + stringOfPermutationsPlus
                self.ui.textEdit.setText(stringOfPermutationsMinus)
                self.ui.result.setText(str(alg2.get_num()))
                print(f"Исходное число1: {num1}\nИсходное число2: {num2}\nПолученный результат: {self.ui.result.text()}")
                print(f"Работа алгоритма: {self.ui.textEdit.toPlainText()}")

    def button_result_strings(self):
        if self.ui.comboBox_strings.currentText()[0] == "1":
            leftWord = self.ui.left_word.text()
            rightWord = self.ui.right_word.text()
            self._newRule = [
                ("@", leftWord, False),
                ("@", "", True)
            ]
            msg = QMessageBox()
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setText(f"Есть пустое слово")
            msg.setWindowTitle("Ошибка")
            if leftWord == "" or rightWord == "":
                msg.exec_()
            else:
                rightWord = "@" + rightWord
                alg = AlgorithmMarkov(word = rightWord, rules = self._newRule)
                self.ui.textEdit_strings.setText(alg.run())
                self.ui.result_word.setText(alg._word)
                print(f"Левое слово: {leftWord}\nПравое слово: {rightWord}\nОжидаемый результат: слом\nПолученный результат: {self.ui.result_word.text()}")
                print(f"Правила замены:{alg._rules}")
                print(f"Работа алгоритма: {self.ui.textEdit_strings.toPlainText()}")

        
        if self.ui.comboBox_strings.currentText()[0] == "2":
            leftWord = self.ui.left_word.text()
            alphabet = [set(self.ui.right_word.text().split(" "))]
            words = [word for set_of_words in alphabet for word in set_of_words]
            alphabet_chars = set(char for word in words for char in word)

            msg = QMessageBox()
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            flag = False
            chars = []
            for char in leftWord:
                if char not in alphabet_chars:
                    flag = True
                    chars.append(char)

            msg.setText(f"Символы '{set(chars)}' не найдены в alphabet")
            msg.setWindowTitle("Ошибка")
            if flag == True or self._newRule == []:
                msg.exec_()
            else:
                self._newRule.append(("@", "", False))
                alg = AlgorithmMarkov(word = leftWord, rules = self._newRule)
                if alg.run() == []:
                    print("Найден цикл")
                    self.ui.result_word.setText("Найден цикл")
                else:
                    self.ui.textEdit_strings.setText(alg.run())
                    self.ui.result_word.setText(alg._word)

    def button_add_rule(self):
        left_zamena = self.ui.left_zamena.text()
        right_zamena = self.ui.right_zamena.text()
        alphabet = [set(self.ui.right_word.text().split(" "))]
        words = [word for set_of_words in alphabet for word in set_of_words]
        alphabet_chars = set(char for word in words for char in word)

        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        flag = False
        chars = []
        for char in left_zamena:
            if char not in alphabet_chars:
                flag = True
                chars.append(char)
        
        for char in right_zamena:
            if char not in alphabet_chars:
                flag = True
                chars.append(char)

        msg.setText(f"Символы '{set(chars)}' не найдены в alphabet")
        msg.setWindowTitle("Ошибка")
        if flag == True or left_zamena == "":
            msg.exec_()
        else:
            self._newRule.append((left_zamena, right_zamena, False)) 
            self.ui.zameni_text.setText(str(self._newRule))

    def button_remove_rule(self):
        del self._newRule[-1]
        self.ui.zameni_text.setText(str(self._newRule))
        

    def changeCombo(self):
        if self.ui.comboBox.currentText()[0] == "1" or self.ui.comboBox.currentText()[0] == "2":
            self.ui.label_num2.hide()
            self.ui.num2.hide()
            self.ui.label_plus.hide()

        if self.ui.comboBox.currentText()[0] == "3":
            self.ui.label_num2.show()
            self.ui.num2.show()
            self.ui.label_plus.show()

        if self.ui.comboBox_strings.currentText()[0] == "1":
            self.ui.right_word.show()
            self.ui.right_label.show()
            self.ui.right_label.setText("Правое слово")
            self.ui.zameni_text.hide()
            self.ui.zameni_label.hide()
            self.ui.addButton.hide()
            self.ui.removeButton.hide()
            self.ui.left_zamena.hide()
            self.ui.right_zamena.hide()
            self.ui.label_arrow.hide()
            self._newRule = []

        if self.ui.comboBox_strings.currentText()[0] == "2":
            self.ui.right_label.setText("Алфавит")
            self.ui.zameni_text.show()
            self.ui.zameni_label.show()
            self.ui.addButton.show()
            self.ui.removeButton.show()
            self.ui.left_zamena.show()
            self.ui.right_zamena.show()
            self.ui.label_arrow.show()
            self._newRule = []

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())