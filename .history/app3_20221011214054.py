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

# file.close()
# -> close the file
