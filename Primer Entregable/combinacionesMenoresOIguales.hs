-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(combinacionesMenoresOiguales(x ::(Integer)))
  }

combinacionesMenoresOiguales :: Integer -> Integer
-- Completar la definición de la función
-- combinacionesMenoresOiguales 1 = 1
-- combinacionesMenoresOiguales 2 = 3 -- i=1, j=1 ; i=1, j=2 ; i=2, j=1; -(i=2, j=2)- 
combinacionesMenoresOiguales n = auxiliar n 1 1
-- Pueden agregan las funciones que consideren necesarias 
auxiliar :: Integer -> Integer -> Integer -> Integer
auxiliar n i j 
  | i > n = 0
  | j > n = auxiliar n (i + 1) 1
  | i * j <= n = 1 + auxiliar n i (j + 1)
  | otherwise = auxiliar n i (j + 1)