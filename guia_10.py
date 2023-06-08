from guia_8 import perteneceStr

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
