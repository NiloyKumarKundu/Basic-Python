# Very Important

# d1 = {
#     "key1": 1,
#     "key2": [1,2,3],
#     "key3": 1.23,
#     "key4": "example"
# }
# print(d1)
# print(type(d1))

# print(d1["key1"])

# # Changable
# d1["key3"] = 45
# print(d1["key3"])


# d2 = {
#     "x": input("enter x: "),
#     "y": input("enter y: ")
# }

# print(d2["x"])


# x = input().split(" ")

# d2 = { }
# d2.update({x[0]: x[1]})

# print(d2[x[0]])

# # d2.clear()
# print(d2)

# del d2[x[0]]
# print(d2)



d2 = {"x": 1}

x2 = d2.keys()
print(x2)

x = d2.values()
print(x)

# keys and values reference niye kaj kore. just view hisebe dekha jabe

d2.update({"y": 2})
print(x)
print(x2)

# both same
p = d2.get("x")
print(p)
p = d2["x"]
print(p)
