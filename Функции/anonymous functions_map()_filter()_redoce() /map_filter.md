#### Анонимные функции, функции map(), reduce(), filter()

- Функция map() применяет функции к элементам итерируемого объекта.
- Функция filter() фильтрует элементы на основе проверяемой функции, требует, чтобы проверочная функция возвращала логическое значение.
- Функция reduce() применяет функции к парам элементов и результатов выполнения, возвращает одиночный результат, применяя функцию к каждому элементу итерируемого объекта.

##### Функция map()

> Пример, например прибавим к каждому элементу списка единицу.
```python
my_numbers = [1, 2, 3, 4]
my_numbers_inc = []

for item in my_numbers:
    item = item + 1
    my_numbers_inc.append(item)

print(my_numbers_inc)
```

Как записать с помощью функции map()
> Синтаксис map(func, iterable, [iterable 2, iterable 3, ...]) 

где ``func`` обозначает функцию, которая будет применена к каждому элементу из ``iterables``. <br>
Количество аргументов функции должно совпадать с количеством ``iterables``.
> Встроенная функция map() реализована очень гибко. В качестве последовательностей мы можем использовать: списки, строки, кортежи, множества, словари.

Теперь как можно написать предыдущий код компактным предыдущий код:
```python
results = list(map(lambda x: x + 1, my_numbers))
print(results) 
```
![image](https://github.com/user-attachments/assets/733a4470-da8c-4b47-888d-25004e49dca3)
![image](https://github.com/user-attachments/assets/8246c598-a4ae-40dd-bfcd-8d3cc0726986)

Другой пример.
```python
print('Код с функцией  map() итерируем циклом for')
def increase(n):
    return n + 1
numbers = [1, 2, 3, 4]
new_numbers = map(increase, numbers)

for n in new_numbers:  # итерируем циклом for
    print(n
```
![image](https://github.com/user-attachments/assets/dfa48527-99a8-4a50-bdce-eba64d80a6ba)

```python
print('Код с функцией  map() преобразуем итератор в список')
def func(elem1, elem2):
    return elem1 + elem2
numbers1 = [1, 2, 3, 4]
numbers2 = [1, 1, 1, 1]
new_numbers = list(map(func, numbers1, numbers2))  #  преобразуем итератор в список
print(new_numbers)
```
![image](https://github.com/user-attachments/assets/91e15bd2-b01a-4345-93a6-5e50cc5ec8f9)

> Если в последовательностях разное количество элементов, то последовательность с минимальным количеством элементов становится ограничителем.
```python
print('Код с функцией  map() преобразуем итератор в список и ограничим данные')
def func(elem1, elem2, elem3):
    return elem1 + elem2 + elem3
numbers1 = [1, 2, 3, 4]
numbers2 = [1, 1]
numbers3 = [1, 2, 3, 4]
new_numbers = list(map(func, numbers1, numbers2, numbers3))  #  преобразуем итератор в список
print(new_numbers)
```
![image](https://github.com/user-attachments/assets/c84d0001-d9a3-4f85-b42e-0026b71bcd55)

Ещё один пример, округление 
```python
circle_areas = [1.25773, 1.37668, 1.51914, 1.60241, 11.11344, 12.212135]

result1 = list(map(round, circle_areas, [1]*6))         # округляем числа до 1 знака после запятой
result2 = list(map(round, circle_areas, range(1, 7)))   # округляем числа до 1,2,...,6 знаков после запятой

print(circle_areas)
print(result1)
print(result2)
```

Результат :
```python
[1.25773, 1.37668, 1.51914, 1.60241, 11.11344, 12.212135]
[1.3, 1.4, 1.5, 1.6, 11.1, 12.2]
[1.3, 1.38, 1.519, 1.6024, 11.11344, 12.212135]
```

##### Функция filter()

Название функции ``filter()`` отвечает само за себя.<br> 
В отличие от ``map()``, которая пропускает каждый элемент через функцию и возвращает результат, ``filter()`` требует, чтобы проверочная функция возвращала логическое значение.

Пример 1
```python
age = [20, 15, 18, 33]
result = list(filter(lambda x: x > 18, age))
print(result)
```

Результат :
```python
[20, 33]
```

Пример 2
```python
names = ["Иван", "Петр", "Ирина", "Николай"]
age = [20, 15, 13, 35]
result = list(map(lambda x, y: (x, y), names, age))
result = list(filter(lambda x: x[1] >= 15, result))
print(result)
или
names = ["Иван", "Петр", "Ирина", "Николай"]
age = [20, 15, 13, 35]
result = list(map(lambda x, y: (x, y), names, age))
result = [x for x in result if x[1] >= 15]
print(result)
```

Результат :
```python
[('Иван', 20), ('Петр', 15), ('Николай', 35)] 
```

Ещё один пример, параметр func указывает ссылку на функцию, которой будет передаваться текущий элемент последовательности.<br> 
Внутри функции func необходимо вернуть значение True или False. Для примера, удалим все отрицательные значения из списка.
```python
print('\nпреобразуем итератор в список')
def func(elem):
    return elem >= 0
numbers = [-1, 2, -3, 4, 0, -20, 10]
positive_numbers = list(filter(func, numbers))  #  преобразуем итератор в список
print(positive_numbers)
```
![image](https://github.com/user-attachments/assets/536f9227-f479-4183-b3db-5d219c14c832)

Преобразование основных типов в булево значение (True/False)
```python
true_values = filter(None, [1, 0, 10, '', None, [], [1, 2, 3], ()])
for value in true_values:
    print(value)
```

Результат :
```python
1
10
[1, 2, 3]
```

##### Функция reduce()
> Синтаксис reduce(func, iterable[, initial]) 
- Параметр func – функция, к которой кумулятивно применяется каждый элемент iterable.
- Значение initial является необязательным и в случае указания, служит стартовым значением или значением по умолчанию, если итерируемый объект пуст.

Напишем программу, которая считает сумму чисел в списке
```python
from functools import reduce # для использования функции reduce() необходимо подключить специальный модуль functools.

numbers = [1, 2, 3, 4, 5, 6]
result = reduce(lambda x, y: x + y, numbers)
print(result)
```

Результат :
```python
21
```
```python
print('а теперь параметру передадим число 5')
numbers = [1, 2, 3, 4, 5, 6]
result = reduce(lambda x, y: x + y, numbers, 5)
print(result)
```

Результат :
```python
26
```




























