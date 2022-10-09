# 1. Getting A User's Input
name:str = input('what is your name: ' )
print('your name is ' + name)

age:int = input('how old are you?: ')
print('your age is ' + str(age))

str_age:str = str(age)

print(f'your name is {name} and {str_age} years old')

# 2. Word Replacement Exercise
sentence:str = input('Enter your sentence: ')
print('your sentence is: ' + sentence)

word1:str = input('Enter the word to replace: ')
word2:str = input('Enter the word to replace is with: ')
print(sentence.replace(word1, word2))


# 3. List In Python
countries:list = ['Korea', 2, 'China', 'United Kingdom', True]
countries2:list = list(('Korea', 2, 'China', 'United Kingdom', True))
countries[0] = 'United States'
countries[3] = 'Canada'
countries[-1] = 'Australia'
print(countries)

print(len(countries))

# 4. List Methods
list1:list = [1, 2, 3, 4, 5]
list2:list = ['banana', 'apples', 'mango', 'orange']

# extend => combine two list together
list1.extend(list2)
print(list1)

# i want to insert 'cherry' into list2 at index 1
list2.insert(1, 'cherry')
print(list2)

# i want to remove particular value from list
list2.remove('banana')
print(list2)

# i want to clear up list2
list2.clear()
print(list2)


# i want to get the index of particular value
# in this case, i want to get the index of 'mango'
list2:list = ['banana', 'apples', 'mango', 'orange', 'mango']
print(list2.index('mango'))

# i want to know how much the item is in the list
# In this case, I want to know how much mango is in the list.
print(list2.count('mango'))

# i want to sort list1 ascending order
list1:list = [4, 3, 5, 1, 2]
list1.sort()
print(list1)

# i want to reverse list1 
list1.reverse()
list2.reverse()
print(list1)
print(list2)

list3 = list2.copy()
print(list3)

print(id(list2))
print(id(list3))

# if i extract an item which is last in the list
print(list1.pop())

# if i want to pop out an item with particular index
print(list2.pop(3))

list2 = ['mango', 'orange', 'mango', 'banana']
# i want to remove an item with particular index
del list2[0]
print(list2)

# if i clear up all list2 
del list2
print(list2)

# but there is different between del and clear
# del => remove object
# clear => not remove object, just clear up all items

# 5. Tuples in Python

three_numbers = (1, 'Hone', True, 3, 1)
three_numbers = tuple((1, 'Hone', True, 3, 1))
# Tuples is immutable object so that i cant modify anythings
# three_numbers[1] = 23
# but list is mutable object so i can modify everthings by using methods

strings = ('home', 'land', 'earth')
print(type(three_numbers))
print(strings)

boo = (True, False, True)
print(boo)

# 6. Functions in Python

def greetings_function(name:str, age:int) -> str:
    print(f'Welcome {name} you are {str(age)} years old!')

greetings_function('yeonuel', 25)
greetings_function(name = 'yeonuel', age = 25)

def greetings_function2(*names:tuple) -> str:
    for i in range(len(names)):
        print(f'welcome {names[i]}')

greetings_function2('john', 'tim', 'tom')

def greetings_function(name:str, age:int) -> str:
    print(f'Welcome {name} you are {str(age)} years old!')

name = input('Enter your name : ')
age = input('Enter your age: ')

greetings_function(name, age)

# 7. The Return Keyword in Python
def add_numbers(num1:int, num2:int) -> int:
    return num1 + num2


num1:int = int(input('Enter first number: '))
num2:int = int(input('Enter second number: '))
print(add_numbers(num1, num2))

# 8. If statements in Python
a = 4
b = 3

if a == True:
    print('A is Ture')

elif a == False:
    print('A is False')

else:
    print('A is none of the two')

boy, short =  True, True
value = input('input a value: ')
# if i write something in input()
# it's automatically transofrom inputted value into string
# so if you want to change that's datatype 
# you have to ues method after using input()
# something like int(input(s)),,,


if type(value) == str:
    print(f'{value} is a string')

# elif type(value) == int:
#     print(f'{str(value)} is an integer')
# elif type(value) == list:
#     print(f'{str(value)} is an list')

else:
    print(f'{str(value)} is not a string')






