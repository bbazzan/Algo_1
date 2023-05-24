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

# print(factorial_5())

# Ej 2
# a
def imprimir_saludo(nombre: str):
    return print("hola", nombre)

# imprimir_saludo("Bruno")

# b
def raiz_cuadrada_de(numero: int) -> float:
    return m.sqrt(numero)

# print(raiz_cuadrada_de(2))

# c
def imprimir_dos_veces(estribillo: str):
    return print(estribillo*2)

# imprimir_dos_veces("muchaaaaaachos!")

# d
def es_multiplo_de(n: int, m: int) -> bool:
    k = n%m
    if k == 0:
        return True
    else:
        return False

# print(es_multiplo_de(5, 4))
# print(es_multiplo_de(8, 4))

# e
def es_par(numero: int) -> bool:
    if es_multiplo_de(numero, 2) == True:
        return True
    else:
        return False

# print(es_par(18))
# print(es_par(19))

# f
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    return m.ceil(comensales*min_cant_de_porciones/8)

# print(cantidad_de_pizzas(5, 4))

# Ej 3
# a
def alguno_es_0(n1: float, n2: float) -> bool:
    return (n1 == 0 or n2 == 0)

# print(alguno_es_0(0, 2))

# b
def ambos_son_0(n1: float, n2: float) -> bool:
    return (n1 == 0 and n2 == 0)

# print(ambos_son_0(0, 0))

# c
def es_nombre_largo(nombre: str) -> bool:
    return (len(nombre) <= 8 and len(nombre) >= 3)

print(es_nombre_largo("Bruno"))