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


```
print("Addition of two complex numbers: ", (4 + 3j) + (3 - 7j))
print ("Subtraction of two complex numbers: ", (4 + 3j) - (3 - 7j))
print ("Multiplication of two complex numbers: ", (4 + 3j) * (3 - 7j))
print ("Division of two complex numbers: ", (4 + 3j) / (3 - 7j))
```

##### Дано два числа a и b. Найдите гипотенузу треугольника с заданными катетами.

> Для примера:

Тест | Ввод | Результат
-----|------|----------
3    |3     |3 
4    |4     |4
     |      |5.0 























