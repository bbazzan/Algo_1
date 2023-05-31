-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(sumaPrimerosNImpares(x ::(Integer)))
  }

sumaPrimerosNImpares :: Integer -> Integer
-- Completar la definición de la función
sumaPrimerosNImpares 1 = 2 * 1 + 2
sumaPrimerosNImpares n = 2 * nEsimoImpar + 2 + sumaPrimerosNImpares (n - 1) 
  where nEsimoImpar = 2 * n - 1
-- Pueden agregan las funciones que consideren necesarias