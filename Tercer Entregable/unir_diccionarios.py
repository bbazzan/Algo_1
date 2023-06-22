from typing import List
from typing import Dict
import json

# funcion que a partir de una lista de diccionarios, los une en un solo diccionario de la forma {clave: [valores]}
# si las claves se repiten, los valores se agregan a la lista de valores de la clave

def unir_diccionarios(a_unir: List[Dict[str,int]]) -> Dict[str,List[str]]:
  # Implementar esta funcion
  
  diccionarios: Dict[str,List[str]] = {}
  
  for diccionario in a_unir:
    for clave in diccionario:
      if clave in diccionarios:
        diccionarios[clave].append(diccionario[clave])
      else:
        diccionarios[clave] = [diccionario[clave]]
        
  return diccionarios

if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))