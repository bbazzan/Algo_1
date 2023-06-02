import sys

def quienGana(j1: str, j2: str) -> str : 
    #Implementar esta funcion
    
    if j1 == j2:
      res: str = "Empate"
    
    if j1 == "Piedra":
      if j2 == "Papel":
        res: str = "Jugador2"
      elif j2 == "Tijera":
        res: str = "Jugador1"
    
    if j1 == "Papel":
      if j2 == "Piedra":
        res: str = "Jugador1"
      elif j2 == "Tijera":
        res: str = "Jugador2"
    
    if j1 == "Tijera":
      if j2 == "Piedra":
        res: str = "Jugador2"
      elif j2 == "Papel":
        res: str = "Jugador1"
    
    return res

if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))