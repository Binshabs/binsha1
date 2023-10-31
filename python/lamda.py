# s=lambda a,b:a*b
# print(s(10,5))

# s=lambda a,b:a+b
# print(s(10,5))

# s=lambda a,b:a/b
# print(s(10,5))

# s=lambda a,b:a+b
# z=s(10,5)
# print(z)



"""lambda and function"""



# def fun(a):
#     return lambda b:a+b
# x=fun(3)
# print(x(5))


def fun(a):
    return lambda b:a*b
x=fun(2)
print(x(3))