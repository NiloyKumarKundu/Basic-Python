# String formating

# a = 10
# str = "hello world" + str(a)
# print(str)
# print(a)

# another way

b = "11"


# print(f"Hello {b} this is {b}" )
# print("Hello"+str(b))



# Set
set1 = {"apple", "orange", "carambola"}

"""
-> Unordered
-> No duplicates
-> Unchangable
"""

# print(set1[0])       #error

# if "apple" in set1:
#     print("YES!")
# else:
#     print("NO\n")


# for x in set1:
#     print(x)

# value add in set
# set1.add("Bananna")
# print(set1)

# value add in set by charecter
# set1.update("lichu")
# print(set1)


# set1 = list(set1)
# set1.append("bannana")
# set1 = set(set1)
# print(set1)


# remove item from set
# set1.remove("bannana")
# print(set1)


#sotorkokari function

# print(set1)
# set1.pop()
# print(set1)
# x = set1.pop()
# print(x)
# print(set1)
# set1.pop()

# delete all item
# set1.clear()
# print(set1)

# delete the set
# del set1
# print(set1)

# string
"""
array
finite length
unchangeable
order
duplicates
slicing
negative indexing
python has no char type data type, it is only a string with lenght 1, ex: "a"
"""


str1 = "Hello World"
str2 = 'Hello World'

str1multi = """ Hello
World"""

str2multi = '''Hello
World
'''

# print(str1 + " " + str2 + " " + str1multi + " " + str2multi)


# string access
# print(str1[0])
# print(str1[1])
# print(str1[2])
# print(str1[3])
# print(str1[4])


# str1[0] = "b"       #error


# slice
# a = str1[0:4]
# print(a)

# a = str1[1:]
# print(a)

# a = str1[:3]
# print(a)

a = "J" + str1[1:]

str1 = a


# convert to list
# list = list(str1)
# list[0] = "H"
# str1 = str(list)
# print(str1)


# str1 = "hello"
# str1 = str1.upper()
# print(str1)
# str1 = str1.lower()
# print(str1)

# str1 = "     J" + str1[1:] + "      "
# str1 = str1.strip()
# print(str1)
# print(len(str1))


# negative indexing in string
str1 = "Hello World"
# print(str1[-1])

# print(str1[-5:-1])
# print(str1[-5:])

# print(str1[-len(str1):])


# loop in string

for x in str1:
    print(f"{x}", end="")
print()


# list
"""
ordered
mutable (changable)
allow duplicates
allow slicing
has negative index
[] means list
allow nesting
"""


# list1 = [1, 2, 3, 4]

# print(list1[0])
# print(list1[1])
# print(list1[-3])

# list1[0] = "niloy"
# print(list1[0])

# set and list e eke sathe j kono variable rakha possible

# list2 = ["", 1, 2, 3.12, (0, "value", 1.0), True, [1,2,3,4]]
# print(list2)


# x = input("Enter some values:").split(" ")          #make input as list
# print(x)
# print(type(x))


# list1 = [1, 2, 3, 4]

# list1.append("name")
# print(list1)
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

x = 4.4567
print(f"{round(x, 3)}")

x = 2
x = x ** 3  #power
print(x)
