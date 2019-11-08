# format seconds to time
print('Введите количество секунд:')

def timing():
    a = int(input())
    if a < 86400:
        print('Вы ввели', a,'секунд') # seconds
        b = a % 3600 # minutes
        c = a // 3600 # hours
        x = b % 60 # seconds left
        y = b // 60 # minutes left
        z = c % 24 # hours left
        # форматирование
        x = "{:02d}".format(x)
        y = "{:02d}".format(y)
        z = "{:02d}".format(z)
        print('В формате HH:MM:SS --->     ', z, ':', y, ':', x)
        print('Повторить? y/n')
        confirm = str(input())
        if confirm == 'y':
            print('Введите количество секунд:')
            timing()
        else:
            print('Завершено')
    else:
        print('Вы ввели количество секунд > 24 часов, введите число меньше 86400')
        timing()
timing()