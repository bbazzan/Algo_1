from typing import List

# Ej 1
### a
def pertenece(s: List[int], e: int) -> bool:
    res: bool = False
    
    for elemento in s:
        if elemento == e:
            res = True
            
    return res

# print(pertenece([1,2,3,4], 5))

def perteneceStr(s: str, e: str) -> bool:
    res: bool = False
    
    for elemento in s:
        if elemento == e:
            res = True
            
    return res

# print(perteneceStr("hola", "h"))

def pertenece2(s: List[int], e: int) -> bool:
    res: List[int] = []
    
    for i in range(len(s)):
        if s[i] == e:
            res.append(1)
        else:
            res.append(0)
            
    cuenta: int = 0
    
    for b in res:
        cuenta += b
    if cuenta != 0:
        return True
    else:
        return False
        
# print(pertenece2([1,2,3, 3, 3,], 14))

### b
def divideATodos(s: List[int], e: int) -> bool:
    res: List[bool] = []

    for i in range(len(s)):
        if s[i] % e == 0:
            res.append(True)
    
    if sum(res) == len(s):
        return True
    else:
        return False

# print(divideATodos([2,4,6,8,10], 2))

### c
def sumaTotal (s: List[int]) -> int:
    res: int = 0
    for e in s:
        res += e

    return res

# print(sumaTotal([1,2,3]))

### d
def ordenados(s: List[int]) -> bool:
    res: List[bool] = []
    
    for i in range(len(s) - 1):
        if s[i] < s[i+1]:
            res.append(True)
        else:
            res.append(False)
        
    if sum(res) == len(s) - 1:
        return True
    else:
        return False

# print(ordenados([1,2,5,4]))

### e
def hayAlgunaDeMasDe7Letras(lista_de_palabras: List[str]) -> bool:
    res: List[bool] = []
    
    for palabra in lista_de_palabras:
        if len(palabra) > 7:
            res.append(True)
        else:
            res.append(False)
    
    if sum(res) != 0:
        return True
    else:
        return False
    
# print(hayAlgunaDeMasDe7Letras(["hola", "mundo", "estetoscopio"]))

### f
def revertirString(string: str) -> str:
    revertido: str = ""
    
    for c in string:
        revertido = c + revertido
        
    return revertido
        
# print(revertirString('Hola'))

def esPalindroma(frase: str) -> bool:
    return frase == revertirString(frase)

# print(esPalindroma("neuquen"))

### g
def fortalezaDeContra(contra: str) -> str:
    if len(contra) < 5:
        return "ROJA"
    elif len(contra) > 8 and tieneAlMenosUnaMayus(contra) and tieneAlMenosUnaMinus(contra) and tieneAlMenosUnNum(contra):
        return "VERDE"
    else:
        return "AMARILLA"

def tieneAlMenosUnaMayus(string: str) -> bool:
    mayusculas: str = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    
    res: bool = False
    
    for c in string:
        if perteneceStr(mayusculas, c):
            res = True
    
    return res
        
# print(tieneAlMenosUnaMayus("alohA"))

def tieneAlMenosUnaMinus(string: str) -> bool:
    minusculas: str = "abcdefghijklmnñopqrstuvwxyz"
    
    res: bool = False
    
    for c in string:
        if perteneceStr(minusculas, c):
            res = True
        
    return res

# print(tieneAlMenosUnaMinus("alohA"))

def tieneAlMenosUnNum(string: str) -> bool:
    numeros: str = "0123456789"
    
    res: bool = False
    
    for c in string:
        if perteneceStr(numeros, c):
            res = True
        
    return res

# print(tieneAlMenosUnNum("pass123"))

# print(fortalezaDeContra("Contrasenia123"))
# print(fortalezaDeContra("contrasenia123"))
# print(fortalezaDeContra("123"))

### h
def saldoFinal(lista_de_movimientos: List[tuple]) -> int:
    saldo_inicial: int = 0
    saldo: int = saldo_inicial
    
    for tupla in lista_de_movimientos:
        if tupla[0] == "I":
            saldo += tupla[1]
        elif tupla[0] == "R":
            saldo -= tupla[1]
    
    return saldo

# lista_de_movimientos = [("I", 2000), ("R", 20), ("R", 1000), ("I", 300), ("R", 2000)]
# print(saldoFinal(lista_de_movimientos))

### i
def sacarRepetidos(lista: List) -> List:
    res: List = []
    
    for elem in lista:
        if elem not in res:
            res.append(elem)
            
    return res

# print(sacarRepetidos([1,1,2,3,1]))

def tieneAlMenos3VocalesDistintas(palabra: str) -> bool:
    vocales: str = "aeiou"
    vocales_en_palabra: List[str] = []
    
    res: bool = False
    
    for c in palabra:
        if perteneceStr(vocales, c):
            vocales_en_palabra.append(c)
    
    vocales_sin_repetir: List[str] = sacarRepetidos(vocales_en_palabra)
    
    if len(vocales_sin_repetir) > 3:
        res = True
    
    return res

# print(tieneAlMenos3VocalesDistintas("murcielago"))

# Ej 2
# a
def pone0sEnPosicionesPares(lista: List[int]) -> List[int]:
    for i in range(len(lista)):
        if i%2 == 0:
            lista[i] = 0
    
    return lista

# print(pone0sEnPosicionesPares([1,2,3,4,5,6,7,8,9]))

# b
def nuevaListaCon0sEnPosicionesPares(lista: List[int]) -> List[int]:
    res = lista
    
    for i in range(len(lista)):
        if i%2 == 0:
            lista[i] = 0
    
    return res

# l = [1,2,3,4,5,6,7,8,9]
# print(l)
# print(nuevaListaCon0sEnPosicionesPares(l))

# c
def remueveVocales(texto: str) -> str:
    res = ""
    vocales = "aeiou"
    
    for letra in texto:
        if not (perteneceStr(vocales, letra)):
            res += letra
    
    return res

# print(remueveVocales("hola mundo"))

# d
def reemplazaVocales(texto: str) -> str:
    res = ""
    vocales = "aeiou"
    
    for letra in texto:
        if (perteneceStr(vocales, letra)):
            res += "_"
        else:
            res += letra
    
    return res

# print(reemplazaVocales("hola mundo"))

# e
# lo hice en el 1)f)
