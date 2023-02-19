# словари - dict, множества - set
# {key: value}

# from random import choice
#
# students = [13, 10, 11, 6, 7, 14, 5, 12, 4, 1, 2, 8]
#
# rates = {}
#
# while len(students) != 0:
#     chosen = choice(students)
#     name = input(f'укажите имя для {chosen}: ')
#     rate = int(input(f'Поставьте оценку для {name}'))
#     rates[name] = rate
#     students.remove(chosen)
#
# for k, v in rates.items():
#     print(f'{k}: {v}')


# menu = {
#     'pizza': {"колбаса", "тесто", "сыр"},
#     'manty': {"тесто", "мясо", "лук"}
# }
#
# while True:
#     user = set(input('введите ингридиент блюда: ').split())
#     print(user)
#     for name, ingridients in menu.items():
#         if not user.difference(ingridients):
#             print(name)

    # user = input('введите название блюда: ')
    # if user in menu:
    #     print(menu[user])
    # else:
    #     print(f'блюда с названием {user} нет'
    #           f'\n все блюда: {menu.keys()}')





#
# print(pizza.intersection(manty))
# print(pizza & manty)
#
# print(pizza.difference(manty))
# print(pizza - manty)
#
# print(pizza.union(manty))
# print(pizza | manty)
#
# print(pizza.symmetric_difference(manty))
# print(pizza ^ manty)


# numbers = [1, 2, 3, 2, 1, 3, 4]
# numbers1 = {1, 2, 3, 2, 1, 3, 4}
#
# numbers1.add(1)
#
# print(numbers1)
# print(type(numbers1))


# new = dict([[2, 'two'], [3, 'three']])
# new = dict(enumerate([2, 'two', 3, 'three']))
# new = dict(name='Samat', age=19, country='kgz')
# print(new)

# student = {
#     'name': 'John',
#     'age': 20,
#     'height': 1.78,
#     'married': True,
#     'hobby': ['chess', 'football', 'books'],
#     'education': ('School', 'University')
# }

'''delete'''
# del student['hobby']
# deleted = student.pop('education')
# print(deleted)
# student['hobby'][0] = 'tennis'
# student['education'] = list(student['education'])
# del student['education'][0]
# student['education'] = tuple(student['education'])

'''edit'''
# student['hobby'].remove('football')
# student['education'] += ('english',)

"""add"""
# student['weight'] = 70
# student['age'] += 1
# student['hobby'].append('TV')
# student.update(new)

# for i in student:
#     print(f'{i} ==> {student[i]}')
#
# for k, v in student.items():
#     print(f"{k}: {v}")

# print(student.keys())
# print(student.values())
# print(student.items())

# print(student.get('height', 'неверный ключ'))

# medetbek: 1
# davlet: 5
# bakay: 5
# osman: 3
# islambek: 4
# kudret: 1
# barsbek: 4
# elzar: 1
# sultan: 1
# sainakan: 5
# sultan n: 3
# ivan: 4