
def multiply(a,b):
    print("multiply!")
    return a * b

def round_number(a):
    print("round!")
    return round(a)

def fact(a):
    print("factorial!")
    if round_number(a) == 0:
        return 0
    return multiply(a, fact(a-1))

print(fact(5))
