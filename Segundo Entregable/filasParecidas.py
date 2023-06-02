from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def filasParecidas(matriz: List[List[int]]) -> bool :
  # Implementar esta funcion
  
  filas: int = len(matriz)
  columnas: int = len(matriz[0])
  
  if filas == 1:
    return True
  
  else:
    n: int = matriz[0][0] - matriz[1][0]
    
    for i in range(1, filas):
      for j in range(0, columnas):
        if matriz[i][j] != matriz[i-1][j] - n:
          return False
  
    return True

if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))