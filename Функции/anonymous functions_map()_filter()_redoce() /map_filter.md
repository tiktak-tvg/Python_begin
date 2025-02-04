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
