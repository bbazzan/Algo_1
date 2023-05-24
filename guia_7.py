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

# print(es_nombre_largo("Bruno"))

# d
def es_bisiesto(año: int) -> bool:
    return (es_multiplo_de(año, 400) or (es_multiplo_de(año, 4) and not(es_multiplo_de(año, 100))))

# print(es_bisiesto(1600))

# Ej 4
# 3kg por cada cm hasta 3m
# 2kg por cada cm arriba de 3m
# por ejemplo: 2m pesan 600kg, y 5m pesan 1300kg
# a la fabrica le sirven arboles de entre 400 y 1000kg

def peso_pino(altura_del_pino: int) -> int:
    '''toma la altura del pino y devuleve su peso segun la siguiente regla:
    3kg por cada cm hasta 3m; 2kg por cada cm arriba de 3m'''
    if altura_del_pino <= 300:
        peso = altura_del_pino*3
    else:
        peso = 300*3 + altura_del_pino*2
    
    return peso

def es_peso_util(peso_del_pino: int) -> bool:
    '''determina si un pino es util dependiendo de su peso segun la siguiente regla:
    el pino es util si su peso es mayor a 400kg y menor a 1000kg'''
    return (peso_del_pino >= 400 and peso_del_pino <= 1000)

def sirve_pino(altura_del_pino: int) -> bool:
    '''a partir de la altura del pino determina si el pino es util en base al peso'''
    peso_del_pino: int = peso_pino(altura_del_pino)
    es_util: bool = es_peso_util(peso_del_pino)

    return es_util

# print(sirve_pino(200))

# Ej 5
# a
def devolver_el_doble_si_es_par(n: int) -> int:
    if es_multiplo_de(n, 2):
        return 2*n
    else:
        return n
    
def devolver_valor_si_es_par_sino_el_que_sigue(n: int) -> int:
    if es_multiplo_de(n, 2):
        return n
    else:
        return n+1

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiple9(n: int) -> int:
    if es_multiplo_de(n, 3):
        return n*2
    elif es_multiplo_de(n, 9):
        return n*3
    else:
        return n
    
def nombre_de_mas_de_5_letras(nombre: str) -> str:
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"

def trabajo_o_vacaciones(sexo: str, edad: int) -> str:
    if (sexo == "M" and (edad >= 65 or edad < 18)) or (sexo == "F" and (edad >= 60 or edad < 18)):
        return "Andá de vacaciones"
    else:
        return "Te toca trabajar"

# print(devolver_el_doble_si_es_par(4))
# print(devolver_el_doble_si_es_par(3))
# print(devolver_valor_si_es_par_sino_el_que_sigue(4))
# print(devolver_valor_si_es_par_sino_el_que_sigue(3))
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiple9(21))
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiple9(18))
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiple9(7))
# print(nombre_de_mas_de_5_letras("Bruno"))
# print(nombre_de_mas_de_5_letras("Sol"))
# print(trabajo_o_vacaciones("M", 27))
# print(trabajo_o_vacaciones("M", 13))
# print(trabajo_o_vacaciones("M", 70))
# print(trabajo_o_vacaciones("F", 27))
# print(trabajo_o_vacaciones("F", 6))
# print(trabajo_o_vacaciones("F", 60))

# Ej 6
# a
def imprimir_numeros_del_1_al_10():
    i = 1
    while i <= 10:
        print(i)
        i += 1
    return

# imprimir_numeros_del_1_al_10()

# b
def imprimir_numero_pares_entre_el_10_y_el_40():
    i = 10
    while i <= 40:
        print(i)
        i += 2
    return

# imprimir_numero_pares_entre_el_10_y_el_40()

# c
def imprimir_eco_10_veces():
    i = 0
    while i < 10:
        print("eco")
        i += 1
    return

# imprimir_eco_10_veces()

# d
def cuenta_regresiva_para_despegue(n: int):
    while n > 0:
        print(n)
        n -= 1
    print("Despegue!")
    return

# cuenta_regresiva_para_despegue(10)

# e
def viaje_en_el_tiempo(año_de_partida: int, año_de_llegada: int):
    año = año_de_partida
    while año > año_de_llegada:
        año -= 1
        print("Viajo un año al pasado, estamos en el año", str(año))
    return

# viaje_en_el_tiempo(2023, 2000)
