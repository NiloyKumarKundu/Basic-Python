# print("Hello Niloy", 100)
# print("Welcome")

# name = "Niloy"
# print(name)
# print(name + " is a boy")
# print(name + " is 23")
# print(name + " is from Bangladesh")

# age = 23
# print(name + " is a boy")
# print(name + " is", age)

# print('Hi\nHow are you?')

# name = 'Niloy'
# print(name.upper())
# print(name.lower())
# print(name)
# print(name[0].isupper())
# print(name[0].islower())
# print(len(name))
# print(name.index('o'))
# print(name.replace('i', 'e'))


# print(bin(2))
# print(bin(202))


# from math import *

# print(pow(2, 3))
# print(sqrt(16))


# name = input('Enter your name: ')
# age = input('Enter your age: ')
# print("Your name is " + name + "\nYou are " + age + " years old")





# Word replacement program

# sentence = input('Enter your sentence: ')
# print("Your sentence is " + sentence)
# word1 = input('Enter the word to replace: ')
# word2 = input('Enter the word to repace it with: ')
# print(sentence.replace(word1, word2))




# List []

# countries = ["Bangladesh", "India", "Chaina", 2, True]
# countries = list(("Bangladesh", "India", "Chaina", 2, True))
# print(countries[2])
# countries[0] = "United Kingdom"
# print(countries)
# print(type(countries[3]))
# print(type(countries[4]))


# list1 = [4, 3, 5, 2, 1]
# list2 = ["banana", "apples", "mango", "oranges", "mango"]
# list1.extend(list2)
# list2.append("cherry")
# list2.insert(1, 'cherry')
# print(list2)
# list2.remove('banana')
# print(list2)
# list2.clear()
# print(list2)
# print(len(list2))
# print(list2.index('mango'))
# print(list2.count('mango'))
# list1.sort()
# print(list1)

# list2.reverse()
# print(list2)

# list3 = list2.copy()
# print(list3)

# list2.pop()
# print(list2)
# list2.pop(3)
# print(list2)
# del list2[0]
# print(list2)

# del list2
# print(list2)




# Touples ()

# three_numbers = (1, 2, 3, 1)
# strings = ('home', 'land', 'earth')
# boo = (True, False)
# print(three_numbers)
# print(strings)
# print(boo)




# function 

# def greetings_function(*name):
#     print("welcome " + str(name[1]))

# greetings_function('niloy', 'mehedi', 'siam')

# def my_func():
#     return 5 + 6

# print(my_func())


# Dictionaries {} -> pair of keys and values

# my_dict = {
#     'Name' : 'Niloy',
#     'Nationality' : 'Bangladeshi',
#     'age' : 23,
#     'Qualification' : 'Collage',
#     'Friends' : ['Mehedi', 'Siam', 'So on']
# }

# print(my_dict['Name'])
# print(my_dict)


# While Loop

# i = 1
# while i <= 6:
#     print(i)
#     i += 1


# For Loop

# for letters in "Hello":
#     print(letters)

# myList = ['ji', 'ju', 'jo']

# for values in myList:
#     print(values)





# 2D List 

# myList = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(myList)

# for i in myList:
#     for j in i:
#         print(j, end=' ')
#     print()



# Basic Calculator

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# op = input("Enter Operator: ")


# if op == '+':
#     print("Addition = ", num1 + num2)
# elif op == '-':
#     print("Subtraction = ", num1 - num2)
# elif op == '*':
#     print("Multiplication = ", num1 * num2)
# elif op == '/':
#     print("Division = ", num1 / num2)
# else:
#     print("Invalied Operator")


# Try

# try:
#     x = int(input('Enter an integer: '))
#     print(x)
# except:
#     print('Something went wrong')
# else:
#     print('Nothing went wrong')




# Files

# r+ -> read and write | a -> append

# country_file = open("/Users/niloykumarkundu/Niloy/Competetive Programming/Basic-Python/From Very New/countries.txt", "r")
# # print(country_file.readable())

# for lines in country_file.readlines():
#     print(lines)

# country_file.close()



# Write in files

# country_file = open("/Users/niloykumarkundu/Niloy/Competetive Programming/Basic-Python/From Very New/countries.txt", "w")
# country_file.write('This is the new text')


# Appand

# country_file = open("/Users/niloykumarkundu/Niloy/Competetive Programming/Basic-Python/From Very New/countries.txt", "a")
# country_file.write('This is the new text')



# Objects

# class myClass:
#     x = 5

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # p1 = myClass()
# p1 = Person('Niloy', 23)
# print(p1.name + " ", p1.age)
# del p1.age
# print(p1.age)





# Inheritence

from testing import Student

class Person(Student):
    pass

p1 = Person()
print(p1.name)