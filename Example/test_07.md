# Базовые объектные типы языка Python и работа с ними.

##### Изучите работу функции type() выполнив следующие операторы. Значения типов должны быть выведены.
```
type(None)
type(True)
type(False)
type(1)
print(type(5.3))
type(5 + 4j)
type([1, 5.3, False, 4])
type((1, True, 3, 5+4j))
type(range(5))
type('Hello')
type(b'a')
type(bytearray([1,2,3]))
type(memoryview(bytearray('XYZ', 'utf-8')))
type({'a', 3, True})
type(frozenset({1, 2, 3}))
type({'a' : 32}).
```

*Решение:*
```
print(type(None))
print(type(True))
print(type(False))
print(type(1))
print(type(5.3))
print(type(5 + 4j))
print(type(1,5.3,False,4]))
print(type(1,True,3,5+4j)))
print(type(range(5)))
print(type('Hello'))
print(type(b'a'))
print(type(bytearray([1,2,3])))
print(type(memoryview(bytearray('XYZ','utf-8'))))
print(type({'a', 3, True}))
print(type(frozenset({1, 2, 3})))
print(type({'a':32}))
```

##### Изучите работу с комплексными числами, выполнив следующие операторы:

```
print("Addition of two complex numbers : ",(4+3j)+(3-7j))
print("Subtraction of two complex numbers : ",(4+3j)-(3-7j))
print("Multiplication of two complex numbers : ",(4+3j)*(3-7j))
print("Division of two complex numbers : ",(4+3j)/(3-7j))
```

![image](https://github.com/tvgVita69/python_begin/assets/98489171/3f0562c4-faf4-45de-8039-c88427709753)


|Результат|
|---------|
|Addition of two complex numbers: (7-4j)
|Subtraction of two complex numbers: (1+10j)
|Multiplication of two complex numbers: (33-19j)
|Division of two complex numbers: (-0.15517241379310348+0.6379310344827587j)

*Решение:*
```
print("Addition of two complex numbers: ", (4 + 3j) + (3 - 7j))
print ("Subtraction of two complex numbers: ", (4 + 3j) - (3 - 7j))
print ("Multiplication of two complex numbers: ", (4 + 3j) * (3 - 7j))
print ("Division of two complex numbers: ", (4 + 3j) / (3 - 7j))
```

##### Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами.

>- Для примера:

|Тест | Ввод | Результат
------|------|----------
| 3   |  3   |   3 
| 4   |  4   |   4
|     |      |   5.0  


##### Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами.

*Решение:*
```
import math
a = float(input())
b = float(input())
c = float(math.sqrt(a ** 2 + b ** 2))
print(float(c))
```

##### Дано натуральное число. Выведите его последнюю цифру.

>- Для примера:

|Тест | Ввод | Результат
------|------|----------
| 179 | 179  | 179 
|     |      |   9

*Решение:*
```
num = float(input())
def sl(x):
return x%10
print(sl(int(num)))
```

##### Дано трехзначное число. Найдите сумму его цифр.

>- Для примера:

|Тест | Ввод | Результат
------|------|----------
| 179 | 179  | 179 
|     |      | 17    

*Решение:*
```
n = int(input())
s = 0
while n != 0:
s += n % 10
n = n // 10
print(s)
```

##### N школьников делят K яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику?

>- Для примера:

|Тест | Ввод | Результат
------|------|----------
| 3   |  3   |   3 
| 14  |  14  |   14
|     |      |   4  

*Решение:*
```
n = int(input())
k = int(input())
s = k // n
print(s)
```

##### В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты. За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.

>- Для примера:

|Тест | Ввод | Результат
------|------|----------
| 20  |  20  |   20 
| 21  |  21  |   21
| 22  |  22  |   22
|     |      |   32  

*Решение:*
```
k1 = int(input())
k2 = int(input())
k3 = int(input())
p = (k1 + k2 + k3) % 2
if p == 1:
p = (k1 + k2 + k3) / 2
p += 1
print(round(p))
elif p == 0:
p = (k1 + k2 + k3) / 2
print(round(p))
```






















