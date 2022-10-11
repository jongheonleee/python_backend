# # 1. Try Except In Python
# # this method is going to get automatically get an error
# # and then just print whatever we want to tell the user
# # x = int(input('Input an Integer: '))

# # input not a interget into x
# # print(x)

# # we can solve this issue
# try:
#     x = int(input('Input an integer: '))
#     print(x)

# except:
#     print('Something went wrong')

# else:
#     print('nothing went wrong')

# finally:
#     print('try except finished')

# 2. Reading Files
# file = open('the file that i want to read', 'r')
# file = open('the file that i want to edit', 'w')
# file = open('file', 'a')
# -> i can add in the middle of the file or modify the file or make any changes
#   i just want to append to the ending of the file

# file = open('file', 'r+')
# -> i want to do both reading and writing

# print(file.readable())
# -> it's can be checked that i can read the file or not

# print(file.readline())
# -> i can print first line in the file

# print(file.readlines())
# -> i can print all lines in the file

# for lines in file.readlines():
#   print(lines)

# file.close()
# -> close the file

# 3. Writing Files
# file = 'file that i want to use'
# file.write('this is the new text')
# i can write something in file by using wirte()

# 4. Classes And objects In Python

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


p1 = Person('Yeonuel', 25)
print(p1.name, p1.age)
