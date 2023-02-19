# списки - list, кортежи - tuple

# new = tuple(range(1, 4))
# new = tuple(new)

# object = (1, True, 2.5, False)
# new = object[2:]
# print(new)

# print(len(object))
# print(type(object))


object1 = [10, True, 7.5]
object2 = object1.copy()
#
# print(id(object1))
# print(id(object2))
# print(object1 == object2)
# print(object1 is object2)
#
# object2[0] = False

# print(object1)
# print(object2)

# object1.reverse()
# # object2 = object1[::-1]
# object1.sort()

# word = list('python')
# print(new)
# print(word)


# изменение
# object1[2] = False
# object1[0] += 15
# object1[0]  object1[-1] = object1[-1], object1[0]

# добавление
# object1.append('бишкек')
# object1.insert(2, 555)
# object1.extend(new)

# object1 = [i for i in object1 if type(i) != str] list comprehension
# удаление
# object1.remove(10)
# del object1[0]
# del object1[2:5]
a=object1.pop(-1)
print (object1)


# print(deleted)

# print(type(object))
