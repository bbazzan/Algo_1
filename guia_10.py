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
    
invertirArchivo("test.txt")