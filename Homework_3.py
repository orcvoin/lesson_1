# sum
print('Введите число: ')
a = int(input())
# Способ 1
number = a + (a*10 + a) + (a*100 + a*10 + a)
# Способ 2
b = a*10 + a
c = a*100 + a*10 + a
number_2 = a + b +c
# принт
print(number)
print(number_2)