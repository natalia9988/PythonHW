# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите число в десятичной системе: '))
print(f'Встроенная функция hex -> {hex(num)}')


def to_hex(num):
    hex_digits = "0123456789abcdef"
    hex_str = ""
    while num > 0:
        hex_str = hex_digits[num % 16] + hex_str
        num = num // 16
    return '0x'+ hex_str
print(f'Собственная функция -> {to_hex(num)}')