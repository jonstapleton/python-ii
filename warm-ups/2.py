from random import randint

def mystery(a):
    b = 4
    if a < 5:
        return a * b + 30
    elif a > 5:
        return a * b - 30
    else:
        return a * b

b = randint(0,10)
b = mystery(b)
print(b)
