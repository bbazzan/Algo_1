import sys

def fibonacciNoRecursivo(n: int) -> int:
  # Implementar esta funcion
  
  a: int = 0
  b: int = 1
  c: int = 0
  
  if n == 0:
    return a
  elif n == 1:
    return b
  else:
    for i in range(0,n):
      c = a + b
      a = b
      b = c
    return a

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))