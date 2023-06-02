from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  # definir esta función
  
  vueloInicial: Tuple[str, str] = ("", "")
  vueloFinal: Tuple[str, str] = ("", "")
  
  for vuelo in vuelos:
    if vuelo[0] == origen:
      vueloInicial = vuelo
    
    if vuelo[1] == destino:
      vueloFinal = vuelo
    
  if vueloInicial == ("", "") or vueloFinal == ("", ""):
    return -1
  
  if vueloInicial == vueloFinal:
    return 1
  
  ruta: List[Tuple[str, str]] = [vueloInicial]
  
  vueloActual: Tuple[str, str] = vueloInicial
  
  while vueloActual[1] != destino:
    idx: int = buscaVueloPorOrigen(vueloActual[1], vuelos)
    if idx >= 0:
      if vueloActual[1] == vueloInicial[0]:
        return -1
      else:
        vueloActual = vuelos[idx]
        ruta.append(vueloActual)
    else:
      return -1
  
  return len(ruta)    

def buscaVueloPorOrigen(origen: str, vuelos: List[Tuple[str, str]]):
  for i in range(len(vuelos)):
    if vuelos[i][0] == origen:
      return i
  
  return -1

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))