# Работа с числовой системой целых чисел (Integer – тип данных, встречающийся чаще всего). Целое, целочисленный тип данных. 
№ Максимальное значение его составляет 2 147 483 647, а минимальное – -2 147 483 648 при 4 байтах. Если оно занимает 2 байта, то показатели варьируются от -32 768 до 32 767. Он всегда больше или равен типу short, а также меньше или равен типу long.

# Числа в десятичной системе счисления. Десяти́чная систе́ма счисле́ния — позиционная система счисления по целочисленному основанию 10. 
# Одна из наиболее распространённых систем. В ней используются цифры 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, называемые арабскими цифрами. 
# Предполагается, что основание 10 связано с количеством пальцев на руках у человека.
# Десятичная система счисления. Используется в повседневной жизни и является самой распространенной. 
# Все числа, которые нас окружают представлены в этой системе. В каждом разряде такого числа может использоваться только одна цифра от 0 до 9.
# Перевод в десятичную систему счисления
# Преобразовать число из любой системы счисления в десятичную можно следующим образом: каждый разряд числа необходимо умножить на Xn, где X - основание исходного числа, n - номер разряда. Затем суммировать полученные значения.
# abcx = (a*x2 + b*x1 + c*x0)10

dec1 = 8
dec2 = 42
dec3 = -3
dec4 = 25802836572356723058203845293402834028304820938402834023580235777082489436236

print(dec1)
print(dec2)
print(dec3)
print(dec4)
print()

# Числа в шестнадцатеричной системе счисления. Шестнадцатери́чная система счисления — позиционная система счисления по основанию 16. 
# В качестве цифр этой системы счисления обычно используются цифры от 0 до 9 и латинские буквы от A до F. 
# Буквы A, B, C, D, E, F имеют значения 1010, 1110, 1210, 1310, 1410, 1510 соответственно.
# Шестнадцатеричная система счисления. Наиболее распространена в современных компьютерах. 
# При помощи неё, например, указывают цвет. #FF0000 - красный цвет. 
# Для записи числа используются цифры от 0 до 9 и буквы A,B,C,D,E,F, которые соответственно обозначают числа 10,11,12,13,14,15.
hex1 = 0x9
hex2 = 0xA
hex3 = 0xFF
hex4 = 0x3de

print(hex1)
print(hex2)
print(hex3)
print(hex4)
print()

# Число в двоичной системе счисления. Двоичная система счисления — позиционная система счисления с основанием 2. 
# Благодаря непосредственной реализации в цифровых электронных схемах на логических вентилях, двоичная система используется практически во всех современных компьютерах и прочих вычислительных электронных устройствах.
# Используется в повседневной жизни и является самой распространенной. Все числа, которые нас окружают представлены в этой системе. В каждом разряде такого числа может использоваться только одна цифра от 0 до 9.
bin1 = 0b11101101
print(bin1)
print()

# Число в восьмеричной системе счисления. Восьмеричная система счисления. Также иногда применяется в цифровой технике. Для записи числа используются цифры от 0 до 7.
oct1 = 0o765
print(oct1)
print()

# построение целого числа из другого значения
string = "15"
number = int(string)
print(number)
print(number + 5)
# string + 5 -- ошибка

# Для проверки вхождения элемента в список используется операция in

# Создание списка
my_list = [5, 7, 9, 1, 1, 2]

# Ввод значения
value = int(input('Введите число: '))

# Проверка, находится ли данное число в списке
if value in my_list:
    print('Число входит в список')
else:
    print('Число не входит в список')

# Ввод строки
string = input('Введите строку: ')

# Проверка, есть ли в данной строке символ q
if 'q' in string:
    print('В этой строке есть символ "q"')
else:
    print('В этой строке нет символа "q"')


