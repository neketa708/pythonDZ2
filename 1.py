"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""
num = int(input("число "))
print(f"Шестнадцатеричное представление числа: {format(num, 'x')}")
print(f"Проверка результата: {hex(num)}")