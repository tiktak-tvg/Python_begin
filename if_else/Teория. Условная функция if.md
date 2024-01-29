# Условная функция if
##### Синтаксис инструкции.
- Оператор-выражение if
![image](https://github.com/tvgVita69/python_begin/assets/98489171/6d372d9f-fa6f-4bba-af2b-f7810601af71)

- Оператор-выражение if-else
![image](https://github.com/tvgVita69/python_begin/assets/98489171/07a93b02-97eb-4ca8-a30c-b6a6f25b84f5)

- Оператор-выражение if-elif-else
![image](https://github.com/tvgVita69/python_begin/assets/98489171/f3f37702-6fb2-4930-9e79-3759c73e9c6e)

```
num = 11
if num > 10:
    print("Число больше 10")
```

```
num = 9
if num > 10:
    print("Число больше 10")
else
    print("Число меньше 10")
```

```
num = 10
if num > 10:
    print("Число больше 10")
elif num < 10:
    print("Число меньше 10")
else:
    print("Число равно 10")
```

![image](https://github.com/tvgVita69/python_begin/assets/98489171/a34b8b95-d83d-4d10-b9b2-9d1cfb52e646)

Можно использовать и тернарные выражения.
```
>>> num = 10
>>> a = print('Число больше 10') if num > 10 else print('Число меньше 10') if num < 10 else print("Число равно 10")
Число равно 10
>>> num = 11
>>> a = print('Число больше 10') if num > 10 else print('Число меньше 10') if num < 10 else print("Число равно 10")
Число больше 10
>>> num = 1
>>> a = print('Число больше 10') if num > 10 else print('Число меньше 10') if num < 10 else print("Число равно 10")
Число меньше 10
>>>
```

![image](https://github.com/tvgVita69/python_begin/assets/98489171/b796a1e4-e338-4acc-bf91-f215d96c270b)

Применение ``input()``
> Например введём ``тернарные условные операторы``:

```
Пример 1.
text = input()
if "ернар" in text:
    print("Встретилось 'ернар' в предложении: ", text)
else:
    print("'тернар' не найдено.")

>?тернарные условные операторы
Встретилось 'ернар' в предложении:  тернарные условные операторы

Пример 2.
text = input()
if "Встрет" in text:
    print("Встретилось 'Встрет' в предложении: ", text)
else:
    print("'Встрет' не найдено.")

>?тернарные условные операторы 
'Встрет' не найдено.
```

##### В Python нет встроенного оператора ``switch/case``. Вместо этого приходится использовать условный оператор ``if``.

> Такой код как наример в C#
```
switch (day) {
    case "Понедельник":
        System.out.println("Первый день недели.");
        break;
    case "Tuesday":
        System.out.println("Второй день недели.");
        break;
    // и так далее
    default:
        System.out.println("Неизвестный день");
}
```

> В Python заменяется таким 

```
Пример 1.
day = 'Вторник'
if day == "Понедельник":
    print("Первый день недели.")
elif day == "Вторник":
    print("Второй день недели.")
elif day == "Вторник":
    print("Третий день недели.")
elif day == "Среда":
    print("Четвертый день недели.")
elif day == "Четверг":
    print("Пятый день недели.")
elif day == "Пятница":
    print("Шестой день недели.")
elif day == "Суббота":
    print("Седьмой день недели.")
elif day == "Воскресенье":
    print("Второй день недели.")
else:
    print("Неизвестный день")
Второй день недели.

Пример 2.
day = 'Суббота'
if day == "Понедельник":
    print("Первый день недели.")
elif day == "Вторник":
    print("Второй день недели.")
elif day == "Вторник":
    print("Третий день недели.")
elif day == "Среда":
    print("Четвертый день недели.")
elif day == "Четверг":
    print("Пятый день недели.")
elif day == "Пятница":
    print("Шестой день недели.")
elif day == "Суббота":
    print("Седьмой день недели.")
elif day == "Воскресенье":
    print("Второй день недели.")
else:
    print("Неизвестный день")
Седьмой день недели.
```
> Или как альтернативу оператору switch/case — использование словарей.

```
def monday():
    return "Второй день недели."
def tuesday():
    return "Третий день недели."
def wednesday():
    return "Четвертый день недели."
def thursday():
    return "Пятый день недели."
def friday():
    return "Шестой день недели."
def saturday():
    return "Седьмой день недели."
def sunday():
    return "Первый день недели."
def default():
    return "Неизвестный день"
switch = {
    "Понедельник": monday,
    "Вторник": tuesday,
    "Среда": wednesday,
    "Четверг": thursday,
    "Пятница": friday,
    "Суббота": saturday,
    "Воскресенье": sunday
}
# использование словаря
print(switch.get(day, default)())
Седьмой день недели.
```
##### Вложенные конструкции.

Любое количество блоков ``if…elif…else`` можно разместить внутри другого оператора ``if…elif…else``
> Например:
- Оператор if внутри другого if-оператора

![image](https://github.com/tvgVita69/python_begin/assets/98489171/69a14337-d69f-4067-8220-47272003ab89)

```
num = float(input("Введите число: "))
if num >= 0:
    if num == 0:
        print("0")
    else:
        print("Положительное число")
else:
    print("Отрицательное число")
Введите число: >? 5
Положительное число

num = float(input("Введите число: "))
if num >= 0:
    if num == 0:
        print("0")
    else:
        print("Положительное число")
else:
    print("Отрицательное число")
Введите число: >? -1
Отрицательное число

num = float(input("Введите число: "))
if num >= 0:
    if num == 0:
        print("0")
    else:
        print("Положительное число")
else:
    print("Отрицательное число")
Введите число: >? 0
0
```
или в одну строку
```
>>> a = 55
>>> b = f'{a} < 50' if a < 50 else (f'{a} > 60' if a > 60 else f'50 > {a} < 60')
>>> print(b)
50 > 55 < 60
>>> a = 45
>>> b = f'{a} < 50' if a < 50 else (f'{a} > 60' if a > 60 else f'50 > {a} < 60')
>>> print(b)
45 < 50
>>> a = 65
>>> b = f'{a} < 50' if a < 50 else (f'{a} > 60' if a > 60 else f'50 > {a} < 60')
>>> print(b)
65 > 60
>>>
```
![image](https://github.com/tvgVita69/python_begin/assets/98489171/60e1298a-4c5a-4830-83ed-119c1b4c054f)

> Другой пример:
- Оператор if-else внутри условия else

 ![image](https://github.com/tvgVita69/python_begin/assets/98489171/460a762b-ff8b-4c43-ab74-8d5cdb5e20f0)
 
```
x = 5
if x > 7:
    print("x больше 7")
else:
    print("x не больше 7")
    if x % 2 == 0:
        print("x - четное число")
    else:
        print("x - нечетное число")
```











