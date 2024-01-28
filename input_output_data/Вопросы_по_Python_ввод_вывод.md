# Вопросы по Python ввод и вывод.
##### 1.Как объявить многострочную строку? Выберите несколько вариантов.
[X]- a.phrase = '''Это многострочная строка'''
-[ ]b.phrase = <Это многострочная строка>
[X]c.phrase = """Это многострочная строка"""

>- Правильные ответы:
phrase = '''Это многострочная строка'''<br>
phrase = """Это многострочная строка"""

##### 2.Выберите правильные варианты форматирования строк.
- [ ]a.city ='Moscow'<br>
country ='Russia'<br>
phrase =f'(city) is the capital of (country)'<br>
- [ ]b.city ='Moscow'<br>
country ='Russia'<br>
phrase ='{1} is the capital of {2}'.format(city, country)<br>
- [X]c.city ='Moscow'<br>
country ='Russia'<br>
phrase =f'{city}is the capital of{country}'<br>
- [X]d.city ='Moscow'<br>
country ='Russia'<br>
phrase ='{0} is the capital of {1}'.format(city, country)<br>

>- Правильные ответы: 
city ='Moscow'<br>
country ='Russia'<br>
phrase =f'{city}is the capital of{country}'<br>
city = 'Moscow'<br>
country = 'Russia'<br>
phrase = '{0} is the capital of {1}'.format(city, country)

##### 3.Какой символ отвечает за переход на новую строку?
- [ ]a.\nl
- [X]b.\n 
- [ ]c.\x
- [ ]d.\t

>- Правильный ответ: \n

##### 4.Что выведет на экран код?
print
(10,'10')
- [ ]a.10
- [ ]b.1010
- [ ]c.Ошибку
- [X]d.10 10

>- Правильный ответ: 10 10

##### 5.Какая функция служит для вывода значений на экран?
- [X]a.print() 
- [ ]b.draw()
- [ ]c.show()

>- Правильный ответ: print()
