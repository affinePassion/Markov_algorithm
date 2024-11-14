from typing import List
from markov import AlgorithmMarkov
from rules import Rules

def main():
    rule1 = Rules()
    successor = []

        
    print("Алгорифмы Маркова")
    print("1. Увеличение числа на единицу")
    print("2. Уменьшение числа на единицу")
    print("3. Сложение чисел")
    print("4. Изменение слова")
    print("5. Слияние двух слов")
    print("6. Убрать первую букву слова")
    print("7. Выход")
    
    try:
        numTask = int(input("Введите номер алгоритма(1..7): "))
        if numTask < 1 or numTask > 7:
            raise ValueError("Номер алгоритма должен быть от 1 до 7")
        if numTask == 7:
            exit()
        if numTask == 1 or numTask == 2:
            algMark = AlgorithmMarkov(word="@100@", rules=rule1.rules_for_digits(numberTask=numTask))
        print(algMark.run())
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()