# lambda, работа с исключениями
# lambda arguments: expression
# try:
#     code
# except:
#     message
# finally:
#     message
# from random import choice
# students = [13, 10, 11, 6, 7, 14, 5, 12, 4, 1, 2, 8]
#
# rates = {}
#
# while len(students) != 0:
#     chosen = choice(students)
#     name = input(f'укажите имя для {chosen}: ')
#     try:
#         rate = int(input(f'Поставьте оценку для {name}'))
#         if rate > 5 or rate < 1:
#             print('оценка должнга быть от 1 до 5')
#             continue
#         rates[name] = rate
#     except:
#         print('введите цифру')
#         continue
#     students.remove(chosen)
#
# for k, v in rates.items():
#     print(f'{k}: {v}')


# numbers = [1, 2, 3]
#
# while True:
#     index_input = input('введите число')
#     if index_input.isdigit():
#         index_input = int(index_input)
#         if index_input <= 2:
#             print(numbers[index_input])
#         else:
#             print('введите корректные данные')
#     else:
#         print('введите корректные данные')
    # try:
    #     index_input = int(input('введите индекс: '))
    #     print(numbers[index_input])
    # except:
    #     print('введите только целые числа от 0 до 2')
    # except ValueError:
    #     print('введите только целые числа')
    # except IndexError:
    #     print("такого индекса нет")



# try:
#     print(5 // 2)
# except:
#     print('не делим на ноль!')
# finally:
#     print("проверка завершена")

# print('123'[4])
# print(number)
# print({1:2}[5])


# objects = ['python', 'geektech', 'bishkek', 'oop', 'tt']
#
# objects.sort(key=lambda x: len(x), reverse=True)
# print(objects)


# numbers = list(range(1, 21))
# new_numbers = [i * 2 for i in numbers if i % 2 == 0]

# new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# new_numbers = tuple(map(lambda x: x * 2, new_numbers))

# print(numbers)
# print(new_numbers)

# x = lambda a, b: a + b
# def z(a, b):
#     return a + b
#
# print(x(2, 3))
# print(z(4, 6))

# def show_words(words_list: list, func):
#     for i in words_list:
#         print(func(i))
#
#
# show_words1 = lambda words: [i.title() for i in words]
# print(show_words1(['rex', 'tom', 'jerry']))
#
#
# def up_letter(word: str):
#     return word.title()
#
#
# def last_up(word):
#     return word[:-1] + word[-1].title()


# show_words(objects, up_letter)
# show_words(objects, last_up)
#
# show_words(('class', 'input', 'polo'), lambda x: x.upper())
