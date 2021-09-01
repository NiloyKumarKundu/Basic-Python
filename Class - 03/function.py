def HelloFun():
    pass            #its like a placeholder

def fun2(x = "default", y = "default2"):
    print("This is for fun", x)
    return [1, 2, 3, "34343we"]

HelloFun()
x = fun2()
x = fun2("arg")
print(x)
