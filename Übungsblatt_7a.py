# Aufgabe 1

def quadrat(x=None):
    if x == None:
        return None
    return x**2

print(f"{quadrat(10)=}")


# Aufgabe 2

def addition(erster_summand,zweiter_summand,*weitere_summanden):
    summe = erster_summand + zweiter_summand 
    for summand in weitere_summanden:
        summe += summand
    return summe

print(f"{addition(3,4)=}")
print(f"{addition(4,5,6,7,8)=}")

# Aufgabe 3-6:

def quad_func(x,a=1,b=1,c=1):
    return a*x**2 + b*x + c

for x in range(11):
    print(f"{quad_func(x,1,2,3)=}")

print(f"{quad_func(10)=}")
print(f"{quad_func(10,5)=}")
print(f"{quad_func(10,c=5)=}")


# Aufgabe 7
# Mit varargs
parameter = (2,3,4)
print(f"{quad_func(10,*parameter)=}")

# Mit kwargs
parameter = {"a":2, "b":3, "c":4}
print(f"{quad_func(10,**parameter)=}")
