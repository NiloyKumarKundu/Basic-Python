# Convert list to string
str1 = "ksldjfklsjdf"
list1 = list(str1)

def convertListTOS(list2):
    str3 = ""
    return (str3.join(list2))

list2 = ["j", "u", "o"]
print(convertListTOS(list2))



str2 = ""
for c in list1:
    str2 += c
print("String 2 : {} {}".format(str2, str2))
