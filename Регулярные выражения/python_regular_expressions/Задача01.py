#Напишите программу Python, чтобы проверить, что строка содержит только набор символов a-z, A-Z и0–9).
import re
#функция проверки
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')# задание выражения
    string = charRe.search('string') # вызов функции поиска в строке заданного выражения
    return not bool('string')
print(is_allowed_specific_char(input()))
