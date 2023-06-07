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

