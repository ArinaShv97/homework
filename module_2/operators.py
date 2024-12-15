first = int (input('Введите целое число: '))
second = int (input('Введите целое число: '))
third = int (input('Введите целое число: '))
if first == second and  first== third and second == third :
    print('3')
elif first == second or second == third :
    print('2')
elif  first != second and  first != third and second != third :
    print('0')