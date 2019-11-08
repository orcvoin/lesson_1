# business
def calculate():
    print('Введите количество выручки')
    income = int(input())
    print('Введите количество издержек')
    outcome = int(input())
    if outcome >= income:
        print('Вы работаете в убыток, пересмотрите бизнес стратегию!!!')
        print('если ошиблись при вводе введите "y"')
        confirm = str(input())
        if confirm == 'y' or 'н':
            calculate()
        else:
            print('Завершено')
    elif income > outcome:
        diff_numb = income - outcome
        diff_perc = outcome / income *100
        print(f'Ваша прибыль составляет: {diff_numb},','затраты составляют:', '{:.2f}'.format(diff_perc) ,'%')
        print('Введите количество сотрудников: ')
        count_boost = diff_numb / int(input())
        print('Прибыль в расчете на сотрудника: ','{:.2f}'.format(count_boost))
calculate()