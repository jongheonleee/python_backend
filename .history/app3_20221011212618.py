# 1. Try Except In Python
# this method is going to get automatically get an eror
# and then just print whatever we want to tell the user
# x = int(input('Input an Integer: '))

# input not a interget into x
# print(x)

# we can solve this issue
try:
    x = int(input('Input an integer: '))


except:
    print('something went wrong,,,, please try again')
