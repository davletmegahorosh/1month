# Функции, аргументы: *args, **kwargs.
# DRY - don't repeat yourself
# definition - определение

# print('125'.isdigit())

# def get_discount(standup: int, hw: int, test: int) -> int:
#     """Принимает стэндапы, дз, тест и возвращает скидку"""
#     if standup >= 8 and 70 <= hw <= 80 and test >= 80:
#         return 3000
#     elif standup >= 8 and 70 <= hw <= 80 and test >= 60:
#         return 2500
#     elif standup >= 6 and 50 <= hw <= 60 and test >= 80:
#         return 2000
#     elif standup >= 6 and 50 <= hw <= 60 and test >= 60:
#         return 2000
#     elif standup >= 6 and 70 <= hw <= 80 and test >= 60:
#         return 2000
#     elif standup <= 6 and 50 <= hw <= 60 and test >= 60:
#         return 1000
#     else:
#         return 'данные неверные или скидки не будет!'
#
# print(get_discount.__doc__)


# timur = get_discount(7, 80, 75)
# azat = get_discount(8, 60, 85)
# azamat = get_discount(4, 30, 45)
# samat = get_discount(8, 80, 100)
#
# list1 = [timur, azat, azamat, samat]
# print(list1)

# def menu(**kwargs):
#     return kwargs
#
# monday = menu(drink='tea', eat='пюре+котлета', dessert='cake')
# print(monday)

# def sum1(a, *args, b=123):
#     # b = args[-2]
#     print(a, b, args)
#     return sum(args)
#
# print(sum1(2, 5, 6, 7, 87, 12, 34, b=56))

# print(len('abc'))
#
# def len1(seq):
#     c = 0
#     for i in seq:
#         c += 1
#     return c
#
# print(2 + len1('ert'))
# print(6 + len1([2, 5, 7, 8]))

# def greeting(name, surname=''):  # name - required parameter
#     print(f'hello, name: {name.title()} surname: {surname.title()}')
#
# greeting('john', 'walker')  # required positional argument
# greeting('samat', 'sadykov')
# greeting(surname='tyson', name='sam')  # keyword arguments
# greeting('alina')


# def get_square(width=1, length=1):
#     return {'width': width, 'length': length, 'square': length * width}
#
#
# class_3 = get_square(4, 7)
# hall = get_square()
# price = 200


# width = 4
# length = 7
# square = width * length
# # print(square)
#
# width = 9
# length = 15
# square = width * length
# print(square)
