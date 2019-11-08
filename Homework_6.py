# 6
print('Введите сколько спортсмен пробежал км за первый день')
first = int(input())
print('Введите количество км для подсчета дней')
total = int(input())
counter = 1

while first <= total:
    first = first * 1.1
    counter += 1
print(counter)



