def tickets():
    child = 3
    adult = 5
    senior = 4
    return child, adult, senior
def maths(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    return x/y

numb1 = int(input("Eneter a Number?"))
numb2 = int(input("Will you enter the second one?"))


ANSWER=subtract(numb1,numb2)
print(ANSWER)
child, adult, senior = tickets()
print(child)
print(adult)
print(senior)