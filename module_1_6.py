my_dict = {'Arina': 1051997,'Sasha':30121995}
print (my_dict)
print (my_dict ['Arina'])
print (my_dict.get('Alex', 'Такого значения нет'))

my_dict.update ({'Masha': 120220024,'Kate': 5051998})
print(my_dict)
a= my_dict.pop('Masha')
print(a)
print(my_dict)


my_set = {'True',1,2,5,1,'Arina',2,2}
print (my_set)
print (my_set.add (10))
print (my_set.add (55))
print (my_set)
print (my_set.discard('Arina'))
print (my_set)