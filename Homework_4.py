# pick highest number
# Способ 1
print('Введите целое положительное число, например от 100 до 10000')
number = int(input())

string = str(number)
max1 = 0
for i in range(len(string)):
    if max1 < int(string[i]):
        max1 = int(string[i])
print(max1)

# Способ 2
max2 = 0
while True:
    z = number % 10
    if z > max2:
        max2 = z
        print(max2)
        break
