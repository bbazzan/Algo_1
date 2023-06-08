from guia_8 import perteneceStr
from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

# Ej 1
# a
def contarLineas(nombre_archivo: str) -> int:
    archivo: str = open(nombre_archivo, 'r')
    lineas: list[str] = archivo.readlines()
    archivo.close()
    return len(lineas)

# print(contarLineas("test.txt"))

# b
def existePalabra(palabra: str, nombre_archivo:str) -> bool:
    res: bool = False
    archivo: str = open(nombre_archivo, 'r')
    lineas: list[str] = archivo.readlines()
        
    for linea in lineas:
        lista_palabras: list[str] = linea.split()
        if perteneceStr(lista_palabras, palabra):
            res = True
    
    archivo.close()
    
    return res

# print(existePalabra("mundo", "/Users/chronos/Documents/Algo_1/test.txt"))

# c
def cantidadApariciones(nombre_archivo: str, palabra: str) -> int:
    res: int = 0
    archivo: str = open(nombre_archivo, 'r')
    lineas: list[str] = archivo.readlines()
        
    for linea in lineas:
        lista_palabras: list[str] = linea.split()
        for p in lista_palabras:
            if p == palabra:
                res += 1
    
    archivo.close()
    
    return res

# print(cantidadApariciones("/Users/chronos/Documents/Algo_1/test.txt", "linea"))

# Ej 2
# funcion que clona un archivo sin cometarios, donde los comentario son aquellas lineas cuando el
# primer caracter es un '#' o espacio en blanco seguido de un '#'

def clonarSinComentarios(nombre_archivo: str) -> None:
    archivo: str = open(nombre_archivo, 'r')
    lineas: list[str] = archivo.readlines()
    archivo.close()
    
    archivo: str = open("clon.txt", 'w')
    
    for linea in lineas:
        if linea[0] != "#" and linea[0] != " " and linea[1] != "#":
            archivo.write(linea)
    
    archivo.close()
    
clonarSinComentarios("test.txt")

# Ej 3
# funcion que dado un archivo, crea uno nuevo pero con las lineas en orden inverso

def invertirArchivo(nombre_archivo: str) -> None:
    archivo: str = open(nombre_archivo, 'r')
    lineas: list[str] = archivo.readlines()
    archivo.close()
    
    archivo: str = open("reverso.txt", 'w')
    
    for i in range(len(lineas) - 1, -1, -1):
        archivo.write(lineas[i])
    
    archivo.close()
    
# invertirArchivo("test.txt")

# Ej 4
# funcion que dado un archivo y una frase (que puede estar separada por '\n' y/o ' '), 
# devuelve el archivo con la frase agregada al final (sin hacer un clon)

def agregarFrase(nombre_archivo: str, frase: str) -> None:
    archivo: str = open(nombre_archivo, 'a')
    archivo.write(frase)
    archivo.close()
    
# agregarFrase("test.txt", "Hola mundo \nHola galaxia \nHola universo")

# Ej 5
# lo mismo que antes pero agregando la frase al principio

def agregarFraseAlPrincipio(nombre_archivo: str, frase: str) -> None:
    archivo: str = open(nombre_archivo, 'r')
    lineas: list[str] = archivo.readlines()
    archivo.close()
    
    archivo: str = open(nombre_archivo, 'w')
    archivo.write(frase)
    
    for linea in lineas:
        archivo.write(linea)
    
    archivo.close()

# agregarFraseAlPrincipio("test.txt", "Hola ciudad \nHola pais \nHola mundo \n")

# Ej 6
# funcion que lee un archivo en binario y devuelve una lista de palabras legibles, donde un plabra legible es
# aquella formada por numero letras mayusculas y/o minusculas y los caracteres esapcio y guion bajo y ademas
# tiene un longitud mayor o igual a 5 caracteres


# Ej 7
# funcio que lee un archivo .csv y calcula el promedio de las notas de los alumnos. El archivo tiene la siguiente
# estructura: lu (str), materia (str), fecha (str), nota (float)

def promedioEstudiante(lu: str):
    archivo: str = open("notas.csv", 'r')
    lineas: list[str] = archivo.readlines()
    archivo.close()
    
    # print(lineas)
    
    notas: list[float] = []
    
    for linea in lineas:
        datos: list[str] = linea.split(",")
        # print(datos)
        if datos[0] == lu:
            notas.append(float(datos[3]))
            
    # print(notas)
    
    suma: float = 0
    
    for nota in notas:
        suma += nota
    
    return suma / len(notas)

# print(promedioEstudiante("448/17"))

# Ej 8
# funcion que genera una lista de n numeros al azar usando random.sample() en el rango [desde, hasta]

def generarNumerosAlAzar(n: int, desde: int, hasta: int) -> list[int]:
    import random
    return random.sample(range(desde, hasta), n)

# print(generarNumerosAlAzar(10, 1, 100))

# Ej 9
# usando la funcion anterior, implemetar una funcion que genere una pila con los numeros generados 

def generarPilaNumerosAlAzar(n: int, desde: int, hasta: int) -> Pila:
    pila: Pila = Pila()
    numeros: list[int] = generarNumerosAlAzar(n, desde, hasta)
    
    for numero in numeros:
        pila.put(numero)
    
    return pila

# print(generarPilaNumerosAlAzar(10, 1, 100).queue)

# Ej 10
# funcion que dada una pila de numeros, devuelve la cantidad de numeros que hay en la pila

def cantidadNumeros(pila: Pila) -> int:
    cantidad: int = 0
    
    while not pila.empty():
        pila.get()
        cantidad += 1
    
    return cantidad

# print(cantidadNumeros(generarPilaNumerosAlAzar(10, 1, 100)))

# Ej 11
# funcion que dada una pila de enteros busca el mayor de ellos y lo devuelve

def buscarMayor(pila: Pila) -> int:
    mayor: int = 0
    
    while not pila.empty():
        numero: int = pila.get()
        if numero > mayor:
            mayor = numero
    
    return mayor

# print(buscarMayor(generarPilaNumerosAlAzar(10, 1, 100)))

# Ej 12
# funcion que dado un string con una formula artimetica, devuelve si los parentesis estan balanceados

def estaBienBalanceada(formula: str) -> bool:
    pila: Pila = Pila()
    
    for caracter in formula:
        if caracter == "(":
            pila.put(caracter)
        elif caracter == ")":
            if pila.empty():
                return False
            else:
                pila.get()
    
    return pila.empty()

# print(estaBienBalanceada("((2+3)*5)"))
# print(estaBienBalanceada("((2+3)*5))"))

# Ej 13
# funcion que, usando generarNmerosAlAzar(), genere una cola con los numeros generados

def generarColaNumerosAlAzar(n: int, desde: int, hasta: int) -> Cola:
    cola: Cola = Cola()
    numeros: list[int] = generarNumerosAlAzar(n, desde, hasta)
    
    for numero in numeros:
        cola.put(numero)
    
    return cola

# print(generarColaNumerosAlAzar(10, 1, 100).queue)

# Ej 14
# funcion que dada una cola de numeros, devuelve la cantidad de numeros que hay en la cola

def cantidadElementos(cola: Cola) -> int:
    cantidad: int = 0
    
    while not cola.empty():
        cola.get()
        cantidad += 1
    
    return cantidad

# print(cantidadElementos(generarColaNumerosAlAzar(10, 1, 100)))

# Ej 15
# funcion que dada una cola de enteros busca el mayor de ellos y lo devuelve

def buscarElMaximo(cola: Cola) -> int:
    mayor: int = 0
    
    while not cola.empty():
        numero: int = cola.get()
        if numero > mayor:
            mayor = numero
    
    return mayor

# print(buscarElMaximo(generarColaNumerosAlAzar(10, 1, 100)))

# Ej 16
# a

def armarSecuenciaDeBingo() -> Cola[int]:
    numeros: list[int] = [i for i in range(0, 100)]
    secuencia: Cola[int] = Cola()
    
    for i in range(0, 100):
        numero = random.choice(numeros)
        secuencia.put(numero)
        numeros.remove(numero)
        
    return secuencia

# b
# funcion funcion que dado un carton de bingo (que es una lista de 12 numeros al azar entre el 0 y el 99)
# y un secuencia de bingo como arriba devuelve el numero de jugadas de de la secuencia necesarias para que ese carton gane,
# es decir que hayan salido los 12 numeros del carton

def jugarCartonDeBingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas: int = 0
    
    while bolillero.empty() == False:
        numero: int = bolillero.get()
        print(numero)
        jugadas += 1
        
        if numero in carton:
            carton.remove(numero)
            print(f'Carton: {carton}')
            
        if len(carton) == 0:
            break
    
    return jugadas

# print("Se necesitan :", jugarCartonDeBingo(generarNumerosAlAzar(12, 0, 99), armarSecuenciaDeBingo()), "jugadas para ganar")

# Ej 17

def generarColaDeGuardia(n: int) -> Cola[(int, str, str)]:
    cola: Cola = Cola()
    
    prioridad: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nombres: list[str] = ["Juan", "Pedro", "Maria", "Jose", "Luis", "Ana", "Lucia", "Carlos", "Miguel", "Sofia"]
    especialidad: list[str] = ["Traumatologia", "Psicologia", "Cardiologia", "Pediatria", "Oftalmologia", "Otorrinolaringologia", "Dermatologia", "Neurologia", "Ginecologia", "Urologia"]
    
    for i in range(n):
        cola.put((random.choice(prioridad), random.choice(nombres), random.choice(especialidad)))
        
    # print(cola.queue)
    
    return cola

def nPacientesUrgentes(c: Cola[(int, str, str)]) -> int:
    cantidad: int = 0
    
    while not c.empty():
        paciente: tuple(int, str, str) = c.get()
        if paciente[0] <= 3:
            cantidad += 1
    
    return cantidad

# print(nPacientesUrgentes(generarColaDeGuardia(10)))

# Ej 18
# funcion que dado un archivo de texto agrupa las palabras por longitud en un diccionario de formato
# {long:cantidad_de_palabras_con_longitud_long}

def agruparPorLongitud(nombre_archivo: str):
    archivo = open(nombre_archivo, "r")
    texto = archivo.read()
    archivo.close()
    palabras = texto.split()
    diccionario = {}
    
    for palabra in palabras:
        longitud = len(palabra)
        if longitud in diccionario:
            diccionario[longitud] += 1
        else:
            diccionario[longitud] = 1
            
    return diccionario

# print(agruparPorLongitud("test.txt"))

