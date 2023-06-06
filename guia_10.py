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
        if perteneceStr(linea, palabra):
            res = True
    
    archivo.close()
    
    return res

print(existePalabra("hola", "test.txt"))