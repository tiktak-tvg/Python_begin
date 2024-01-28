def function(c, d):
    # a, b -- глобальные переменные; c, d -- локальные
    global a, b
    # изменение значения глобальной переменной
    a = 5
    # изменение значения глобальной переменной
    b = 7
    # создание локальной переменной с тем же именем, что и у глобальной
    c = 10
    # создание локальной переменной с тем же именем, что и у глобальной
    d = 12

a, b, c, d = 1, 2, 3, 4  # множественное присваивание
print(a, b, c, d)  # 1 2 3 4
function(c, d)
print(a, b, c, d)  # 5 7 3 4
