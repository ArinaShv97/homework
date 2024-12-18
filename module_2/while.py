my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
new_list = []
while len(my_list) > i:
    if my_list[i] < 0 :
        print('значение отрицательное')
        continue
    new_list.append(my_list[i])
    i = + 1
    print(new_list)
#Не могу понять в чем ошибка, выводит список только 42,69 и до конца 69














