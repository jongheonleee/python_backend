# 1. Building An Even Number Checker Program
# num = int(input('Enter a number: '))

# if num % 2 == 0:
#     print('Even number')

# else:
#     print('Odd number')

# # 2. Dictionaries In Python
# my_dict = {
#     'name': 'Yeonuel',
#     # Dictionaries doesn't allow to use duplicate
#     # 'name': 'John',
#     'name2': 'Yeonuel',
#     'age': 99,
#     'is_tall': True,
#     'nationality': 'South Korea',
#     'qualification': 'College',
#     'friends': ['Peter', 'Paul', 'Precious']
# }


# print(my_dict)

# # len() => treturn he numbers of key in dictionaries
# print(len(my_dict))

# # dictionaries allow to use various of data type as value
# print(my_dict['age'])
# print(my_dict['is_tall'])
# print(my_dict['friends'])

# print(my_dict)
# print(type(my_dict))

# x = my_dict['name']
# print(x)

# 3. While Loops In Python
# i = 1
# while i < 6 or i == 6:
#     print(i)
#     i += 1

# 4. For Loops In Python
# my_list = ['ji', 'ju', 'jo']
# my_dict = {
#     'name': 'Yeonuel',
#     'age': 99,
#     'is_tall': True
# }

# for x in range(3, 7):
#     print(x)

# else:
#     print('Finished Looping!!')

# for values in my_list:
#     if values == 'ju':
#         break

#     print(values)

# for key in my_dict:
# print(key)

# 6. 2D Lists
# my_list = [1, 2, 3, 4]

my_list2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(my_list)
# print(my_list2)
# print(my_list2[0])
# print(my_list2[0][1])


# for list in my_list2:
#     for row in list:
#         print(row)

# 7. Comments In Python
# print('hello')
# print(1)

# 8. Building A Basic Calculator
n1 = int(input('Enter first number :'))
n2 = int(input('Enter second number :'))

op = input('Enter Operator: ')

if op == '+':
    print('the addition is ' + str(n1 + n2))

elif op == '-':
    print('the subtraction is ' + str(n1 - n2))


elif op == '*':
    print('the multification is ' + str(n1 * n2))

elif op == '/':
    print('the division is ' + str(n1//n2))

else:
    print('Invalid operator')
