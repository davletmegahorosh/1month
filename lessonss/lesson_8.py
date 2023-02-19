# 77, 35, 55, 63, 70, 66, 69





from time import sleep

# with open('results.txt', 'w') as file:
#     file.write('')
#
# for i in range(2, 10):
#     for j in range(2, 10):
#         try:
#             user = int(input(f'сколько будет {i} * {j}: '))
#             right_answer = i * j
#             with open('results.txt', 'a') as file:
#                 if user == right_answer:
#                     file.write(f"\n{i} * {j} = {user} ({right_answer}) right")
#                     print('Правильно!')
#                 else:
#                     file.write(f"\n{i} * {j} = {user} ({right_answer}) wrong")
#                     print(f"Неправильно! подсказка: ({right_answer})")
#         except:
#             print('введите только числа!')


# with open('results.txt', 'r') as file:
#     data = []
#     for i in file.readlines():
#         data.append(i.split()[-1])
#
#     rights = data.count('right')
#     wrongs = data.count('wrong')
#     total = len(data)
#
# print(
#     f"правильно: {rights}\n"
#     f"неправильно: {wrongs}\n"
#     f"кол-во вопросов: {total}"
# )



# работа с файлами
# w - перезаписывает
# a - дозаписывает
# r - чтение
# x - если файл есть, выдаёт исключение.

# file = open('file.txt', 'w', encoding='UTF-8')
# file.write('12')
# file.close()

# with open('file.txt', 'x') as file:
#     file.write('python programming language')

# with open('file.txt', 'r') as file:
#     for i in file.read():
#         sleep(1)
#         print(i, end='')
    # print(file.read())
