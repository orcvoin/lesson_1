# learn variables and types
string = """
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.
"""

a = 1
b = 'wolf'
c = False
d = (a, b, c)
f = [a, b, c, str(a)+b, b[1]]
g = {f"{b}": f"{1}"}
print('Введите любой текст:')
x_input = input()
print(f'Тип введенных данных: ', {type(x_input)})
print(f'Тип переменной a: {a}, это {type(a)}')
print(f'Тип переменной b: {b}, это {type(b)}')
print(f'Тип переменной d: {d}, это {type(d)}')
print(f'Тип переменной f: {f}, это {type(f)}')
print(f'Тип переменной g: {g}, это {type(g)}')
print(type(string))