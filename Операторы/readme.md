#### Содержание.

- arithmetic_operations.py
- bool.py
- complex_numbers.py
- dynamic_typing.py
- hello.py
- hello_print().py
- input.py
- integer-example.py
- len.py
- length_of_a_string.py
- logical_operations.py
- print.py
- print_with_name.py
- string_example.py
- string_indexing.py
- string_operations.py
- string_slicing.py
- арифмет_операторы.py
- примеры.md
- сравнения.py

##### Модуль operator

Чтобы не писать каждый раз функции, определяющие такие стандартные математические операции как сумма или произведение.

Список функций из модуля operator выглядит так:

![image](https://github.com/tvgVita69/python_begin/assets/98489171/e80c03e9-60d4-4b3c-9e54-6b4d33fad703)

```python
from operator import *     #  импортируем все функции

print(add(10, 20))         #  сумма
print(floordiv(20, 3))     #  целочисленное деление
print(neg(9))              #  смена знака
print(lt(2, 3))            #  проверка на неравенство <
print(lt(10, 8))           #  проверка на неравенство <
print(eq(5, 5))            #  проверка на равенство ==
print(eq(5, 9))            #  проверка на равенство ==
```

```python
from functools import reduce
import operator

words = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']
numbers = [1, 2, -6, -4, 3, 9, 0, -6, -1]

opposite_numbers = list(map(operator.neg, numbers))    #  смена знаков элементов списка
concat_words = reduce(operator.add, words)             #  конкатенация элементов списка

print(opposite_numbers)
print(concat_words)
```

Результат
```python
[-1, -2, 6, 4, -3, -9, 0, 6, 1]
Testing shows the presence, not the absence of bugs
```
