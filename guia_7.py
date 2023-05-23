import math as m

# Ej 1
# a
def raizDe2() -> float:
    return round(m.sqrt(2), 4)

#raizDe2()

# b
def imprimir_hola():
    return print("hola")

# imprimir_hola()

# c
def imprimir_un_verso():
    return print("muchaaaaaaaachos! \nahora nos volvimo' a ilusionar \nquiero ganar la terceeeeeeera \nquiero ser campeon mundiaaaaaal")

# imprimir_un_verso()

# d
def factorial_2() -> int:
    return 2

# print(factorial_2())

# e
def factorial_3() -> int:
    return 3*factorial_2()

# print(factorial_3())

# f
def factorial_4() -> int:
    return 4*factorial_3()

# print(factorial_4())

# g
def factorial_5() -> int:
    return 5*factorial_4()

print(factorial_5())