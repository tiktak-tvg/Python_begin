# # Модуль 1.
#import math
#x1 = float(input())
#y1 = float(input())
#x2 = float(input())
#y2 = float(input())
#a = math.sqrt((x2-x1)**2+(y2-y1)**2)
#print('{:.3f}'.format(a), sep='')


#a = int(input())
#b = int(input())
#c = int(input())
#print(str(a)+'+'+str(b)+'+'+str(c)+'='+str(a+b+c))
#print(str(a)+'*'+str(b)+'*'+str(c)+'='+str(a*b*c))
#z = (a+b+c)/3
#z = round(z,3)
#print('('+str(a)+'+'+str(b)+'+'+str(c)+')/3='+str(z))

#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())
#print("Ваша сдача составляет",(c * 100 + d - a * 100 - b) // 100,'руб.', (c * 100 + d - a * 100 - b) % 100, 'коп.')

#import math

#x1, y1 = float(input()), float(input())
#x2, y2 = float(input()), float(input())
#a = math.sqrt((x2-x1)**2+(y2-y1)**2)
#print('{:.3f}'.format(a), sep='')
#a = 'Hello World'
#for i in range(len(a)):
#    print(a[i]) # обращение по индексу
#A = int(input())
#B = int(input())

#for i in range(A, B+1):
#    print(i)
#a = int(input())
#b = int(input())
#res = 0
#for _ in range (abs(b)):
#    res += abs(a)
#print(((res, -res), (-res, res))[a>=0][b>=0])

#a = int(input())
#b = int(input())
#from math import sqrt
#for i in range(a, b + 1):
#    if sqrt(i).is_integer():
#      print(i)
#s = 0
#if a < 0 and b < 0:
#    a = -a
#    b = -b
#elif a < 0:
#    a,b = b,a
#    for i in range(a):
#        s += b
#print(s)
# !/usr/bin/python
# -*- coding: utf-8 -*-




#from math import sqrt

#def distance(x1, y1, x2, y2):
#    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#x1 = float(input())
#x2 = float(input())
#y1 = float(input())
#y2 = float(input())

#nzero = 0
#for i in range(int(input())):
#    if int(input()) == 0:
#        nzero += 1
#print(nzero)

#n = int(input())
#number = 1
#while number <= n:
#    if n % number == 0:
#        print(number, end=" ")
#    number += 1
#print()
#n, s = int(input()), 0
#while n: s += n % 10; n //= 10
#print(s)
#num = 0
#element = int(input())
#while element != 0:
#    num += element
#    element = int(input())
#print(num)

#max = 0
#n = -1
#while n != 0:
#    n = int(input())
#    if n > max:
#        max = n
#print(max)

#n = int(input())
#if n == 0:
#    print(0)
#else:
#    a, b = 0, 1
#    for i in range(2, n + 1):
#        a, b = b, a + b
#    print(b)

#p = int(input())
#a = 0
#while p != 0:
#    next = int(input())
#    if next != 0 and p < next:
#        a += 1
#    p = next
#print(a)

#import sys
#def Kvadrat (n) :
#    S = '*'
#for i in range (n) :
#    print (S*n)
#sys. stdout. write()
#Kvadrat (int (input ()))

#def print_square():
#    N = int(input())
#    list(map(print, ['*' * N] * N))
#print_square()

#n = int(input())
#i = 0
#sum = 0
#while i <= n:
#    sum += i**2
#    i += 1
#print(sum)
#n = input()
#n = int(input())
#print("%020.f" % + n)
#print("%024.f" % 10)
#from math import pi
#r = float(input())
#S = pi*r*r
#print('%.3f' %S)
#l=2 * pi * r
#print(f"{l:.3f}")


#a = int(input())
#b = int(input())
#c = int(input())
#print("{}+{}+{}".format(a, b, c, (a+b+c)))
#print("{}*{}*{}".format(a, b, c, (a*b*c)))
#print("{}-{}-{}".format(a, b, c, (a-b-c)))
#a = int(input())
#b = int(input())
#def maximer(a, b):
#
#    c = a // b
#    c = ((c + 2) // (c + 1)) % 2
#    d = (c + 1) % 2
#    res = a * c + b * d
#    print(res)
#    return res
# n = int(input())
# if n ==0 or n > 12:
#     print(0)
# elif n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
#     print(31)
# elif n == 4 or n == 6 or n == 9 or n == 11:
#     print(30)
# elif n == 2:
#     (print(28))

#seasons = {'Winter': (1, 2, 12),
#           'Sping': (3, 4, 5),
#           'Summer': (6, 7, 8),
#           'Autumn': (9, 10, 11)}

#month = int(input('Choose a month: '))
#for key in seasons.keys():
#    if month in seasons[key]:
#        print(key)
#    else:
#         print('NO')


#if __name__ == '__main__':
#    assert maximer(a, b)#

    #x = max(a, b)

    #print(x)  # => 5

    #a = ()
    #y = maximer(a)

    #print(y)  # => 9
# a = int(input())
# var = a != 0
# if   a == 1 or a == 2 or a == 12:
#     print ('winter')
# elif a == 3 or a == 4 or a == 5:
#     print ('sping')
# elif a == 6 or a == 7 or a == 8:
#     print ('summer')
# elif a == 9 or a == 10 or a == 11:
#     print ('autumn')
# else:
#     print ('NO')

# a = str(input())
# if   a == 'abc':
#     print ('YES')
# else:
#     print ('NO')
#
# x = int(input())
# y = int(input())
# z = int(input())
# a = x + z - y
# b = y + z - x
# c = x + y - z
# if all(i > 0 and i & 1 == 0 for i in [a, b, c]):
#     print(a >> 1, 0, a >> 1)
#     print(0, b >> 1, b >> 1)
#     print(c >> 1, c >> 1, 0)
# else:
#     print('Impossible')

#
# x = int(input())
#
#
# if  d == 0:
#     print('YES')
# else:
#     print('NO')

#if  join(x) == 0:
#    print('YES')
#else:
#   print('NO')
# i = 3
# print("9", end="")
# while i < 6:
#     print(i, end="")
#     i += 1
# i = 4
# a = 12
# while i < 5:
#     a += i
#     i += 1
# i = 1
# while True:
#     if i%3 ==0:
#         break
#     print(i)
#     i +=1
# str_1=input()
# s2=str_1.split()
# print(s2[1])
# s=input()
# #a=(s[ : :-1])
# a = s
# if a==s:
#     print("YES")
# else:
#     print("NO")
#print(*(i for i in input().split('\\')),sep='\n')
# x, y, z=input().split()
# print(f'{z.capitalize()} {x[0].upper()}.{y[0].upper()}.')
#print(*(lambda _, a: (min(a, default=-1), max(a, default=-1),))(int(input()), list(filter(lambda x: x > 0 and x % 2 == 0, map(int, input().split())))))
# a = list(map(int, input().split()))
# m = max(a)
# n = len(a)
# for i in enumerate(a.index()):
#     if i == 0:
#        i = 0
# if n % 2 == 0 and n >= 4:
#         b = m
#         print(b)
# else:
#     print('-1')
a = list(map(int, input().split()))
m = max(a)
n = len(a)
#for i in a:
    if a == 0:
        a = 0
        print(i)
        break
    if n >= 4:
        i = m
        print(i)
    else:
        print('-1')










