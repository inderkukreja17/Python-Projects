# def add(*args):
#     print(args[5])
#     total=0
#     for n in args:
#         total+=n
#     return total
#
#
#
# sum=add(3,5,7,5,9,38,27,47)
# print(sum)


def calculate(n,**kwargs):
    # for key,value in kwargs.items():
    #     print(value)
    #     print(key)
    n+=kwargs["add"]
    n*=kwargs["mul"]
    return n
print(calculate(2,add=4,mul=5))

