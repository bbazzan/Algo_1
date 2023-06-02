from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int :
  # Implementar esta funcion
  
  maxMeseta: List[int] = []
  meseta: List[int] = []
  
  if len(l) <= 1:
    res: int = len(l)

  else:
    for i in range(0, len(l)):
      
      if len(meseta) == 0 or l[i] == meseta[0]:
        meseta.append(l[i])
                
      if l[i] != meseta[0]:
        if len(meseta) >= len(maxMeseta):
          maxMeseta = meseta
        meseta = [l[i]]
    
    if len(meseta) > len(maxMeseta):
          maxMeseta = meseta
        
    res: int = len(maxMeseta)
      
  return res

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))