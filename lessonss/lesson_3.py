# циклы: for, while
# break, continue
# ctrl + ?

eng_alphabet = "qwertyuiop[]asdfghjkl;'zxcvbnm,. "
rus_alphabet = "йцукенгшщзхъфывапролджэячсмитьбю "

# while True:
#     user_input = input('\nвведите слово: ')
#     alter = ''
#     if user_input == 'exit' or alter == 'exit':
#         print('программа завершена!')
#         break
#     for i in user_input:
#         print(alter)
#         if i in eng_alphabet:
#             print(rus_alphabet[eng_alphabet.index(i)], end='')
#
#         elif i in rus_alphabet:
#             print(eng_alphabet[rus_alphabet.index(i)], end='')
#             alter += eng_alphabet[rus_alphabet.index(i)]

# else:
#     print('недопустимые символы!')

# print(rus_alphabet[eng_alphabet.index('w')])



# пуулеуср
# c = 0
# while c != 20:
#     c += 1
#     if c == 13:
#         continue
#     if c % 2 != 0:
#         print(c)

    # print('Hello!', c)
    # if c == 500:
    #     break

# n = 5
# while n > 0:
#     print(n)
#     n -= 1


# for i in range(1, 4):
#     for j in range(1, 4):
#         for l in range(1, 4):
#             print(f'{i} {j} {l}')

word = 'kyrgy8z9stan'
counter = 1
#
for letter in word:
    # if letter == '8' or letter == '9':
        if not letter.isdigit():
            # print(letter.upper())
            print(counter, letter)
            counter += 1
            if letter == 'z':
                break
    #         continue
    # print(f'мы нашли число: {letter}')
