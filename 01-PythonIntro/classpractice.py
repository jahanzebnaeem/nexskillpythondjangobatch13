# print(1+1)
# print(len("This is Jahanzeb's pen"))
# print("Naeem")
# fName = "Syed"
# lName = "Nauman"
# s = "This is Jahanzeb's pen"
# print("Welcome to the lecture {l} {f}, hope you are learning something".format(
# f=fName, l=lName))

# my_list = ['one', 'two', 'three', 4, 5]
# print(my_list)
# my_list = my_list + ['new item']
# print(my_list)

# my_list = [1, 2, 3]
# print(my_list * 3)

# l = [1, 2, 3]
# l.append("abc")
# print(l[4])
# l.pop(0)
# print(l)

# new_list = ['a', 'e', 'x', 'b', 'c']
# print(new_list)
# new_list.reverse()
# print(new_list)
# new_list.sort()
# print(new_list)

# lst_1 = [1, 2, 3]
# lst_2 = [4, 5, 6]
# lst_3 = [7, 8, 9]

# matrix = [lst_1, lst_2, lst_3]
# # print(matrix[2][2])

# first_col = [row[0] for row in matrix]
# print(first_col)

# my_dict = {'key1': 123, 'key2': [12, 23, 33],
#            'key3': ['item0', 'item1', 'item2']}

# print(my_dict['key3'])

# d = {'key1': {'nestkey': {'subnestkey': 'value'}}}
# print(d['key1'])
# print(d.keys())

# d = {'key1': 1, 'key2': 2, 'key3': 3}
# print(d.items())

# t = (1, 2, 3, 1, 3, 4, 3, 1)
# print(t.append(3))

# l = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1]

# print(set(l))

# print(1 == "1")

# ages = {"Sam": 3, "Frank": 4, "Dan": 29}

# for key in ages:
#     print("This is the key")
#     print(key)
#     print("This is the value")
#     print(ages[key])
#     print("\n")

# mypairs = [(1, 10), (3, 30), (5, 50)]

# for tup in mypairs:
#     print(tup)

# for item1, item2 in mypairs:
#     print(item1)
#     print(item2)

# for i in range(5):
#     print(i)

# def addEvenOnly(num1, num2):
#     """
#     INPUT: Two numbers
#     OUTPUT: False if both numbers are not even,
#     the sum if both numbers ar even
#     """
#     if (num1 % 2 != 0) or (num2 % 2 != 0):
#         return False
#     else:
#         return num1+num2


# x = addEvenOnly(1, 2)
# y = addEvenOnly(2, 2)
# print(x)
# print(y)

# import random
# digits = list(range(10))
# random.shuffle(digits)
# print(digits[:3])

# guess = input("What is your guess? ")
# print(guess)

x = 50


def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)


print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
