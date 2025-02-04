# Вопросы по Python ввод и вывод.
##### 1.Как объявить многострочную строку? Выберите несколько вариантов.
- [X] a.phrase = '''Это многострочная строка''' &check;
- [ ] b.phrase = <Это многострочная строка>
- [X] c.phrase = """Это многострочная строка""" &check;

> Правильные ответы:
- phrase = '''Это многострочная строка'''
- phrase = """Это многострочная строка"""

##### 2.Выберите правильные варианты форматирования строк.
- [ ] a.city ='Moscow'<br>
country ='Russia'<br>
phrase =f'(city) is the capital of (country)'<br>
- [ ] b.city ='Moscow'<br>
country ='Russia'<br>
phrase ='{1} is the capital of {2}'.format(city, country)<br>
- [X] c.city ='Moscow'<br> &check;
country ='Russia'<br>
phrase =f'{city}is the capital of{country}'<br>
- [X] d.city ='Moscow'<br> &check;
country ='Russia'<br>
phrase ='{0} is the capital of {1}'.format(city, country)<br>

> Правильные ответы: 
- city ='Moscow'<br>
country ='Russia'<br>
phrase =f'{city}is the capital of{country}'<br>
- city = 'Moscow'<br>
country = 'Russia'<br>
phrase = '{0} is the capital of {1}'.format(city, country)

##### 3.Какой символ отвечает за переход на новую строку?
- [ ] a.\nl
- [X] b.\n  &check;
- [ ] c.\x
- [ ] d.\t

> Правильный ответ: \n

##### 4.Что выведет на экран код?
print
(10,'10')
- [ ] a.10
- [ ] b.1010
- [ ] c.Ошибку
- [X] d.10 10 &check;

> Правильный ответ: 10 10

##### 5.Какая функция служит для вывода значений на экран?
- [X] a.print()  &check;
- [ ] b.draw()
- [ ] c.show()

> Правильный ответ: print()

##### 6.Какая команда используется для вывода (печати) данных?
- [ ] a. Console.WriteLine()
- [ ] b. cout()
- [ ] c. printf()
- [X] d. print() &check;
##### 7.Выберите верные строки кода.
- [ ] a. print('Просто текст...")
- [X] b. print() &check;
- [X] c. print("I'm a math teacher and a programmer!") &check;
- [X] d. print('Поэма "Мёртвые души" одна из самых интересных') &check;
- [X] e. print("3.1415") &check;
- [ ] f. print('I'm 16 and I'm from Northern Ireland.')
##### 8.Выберите верные строки кода.
- [ ] a. print("10", '100', '1000)
- [X] b. print('Python', 'is the best', '!!') &check;
- [ ] c. print("раз", "два, "три")
- [ ] d. print("Python", , "is the best")
##### 9.Что выведет следующий код print('1', '2', '3', '4', sep='*')?
- [ ] a. 1 2 3 4
- [ ] b. 1234
- [X] c. 1*2*3*4 &check;
- [ ] d. 24
##### 10.Выберите верные строки кода.
- [X] a. print("Honey, what's your hurry", end='?') &check;
- [X] b. print("The world's a little blurry", "Or maybe it's my eyes", end='!!!', sep=' :) ') &check;
- [X] c. print("Told you not to worry", "But maybe that's a lie", sep=' :) ') &check;
- [ ] d. print("Remember not to get too close to stars", "They're never gonna give you love like ours", sepp=" ")
- [ ] e. print("Remember not to get too close to stars", end=="")
##### 11.Какая команда используется для считывания данных с клавиатуры?
- [ ] a. Console.ReadLine()
- [ ] b. scanf()
- [ ] c. cin
- [X] d. input() &check;
##### 12.Какая из указанных строк считывает целое число в переменную n?
- [ ] a. n = input()
- [ ] b. n = integer(input())
- [X] c. n = int(input()) &check;
- [ ] d. n = number(input())
- [ ] e. n = str(input())
##### 13.Выберите верные утверждения.
- [X] a. Имя переменной может начинаться с символа подчёркивания (_) &check; 
- [ ] b. Имя переменной не может оканчиваться цифрой 
- [X] c. Имя переменной не может совпадать с ключевым (зарезервированным) словом &check;
- [X] d. Имя переменной не может начинаться с цифры &check;
##### 14.Какое число выведет следующий код?
```
s = 13
k = -5
d = s + 2
s = d
k = 2 * s
print(s + k + d)
Вывод
>>> s = 13
>>> k = -5
>>> d = s + 2
>>> s = d
>>> k = 2 * s
>>> print(s + k + d)
60
```

##### 15.Какое число выведет следующий код?
```
a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)
Вывод
>>> a = 17 // (23 % 7)
>>> b = 34 % a * 5 - 29 % 4 * 3
>>> print(a * b)
56
```
