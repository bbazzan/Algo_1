-- Ej 1
-- a
f :: Integer -> Integer
f n 
    | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

-- b
g :: Integer -> Integer
g n 
    | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

-- c 
h :: Integer -> Integer
h n = f (g n) 

k :: Integer -> Integer
k n = g (f n)

-- Ej 2
-- a
absoluto :: Integer -> Integer
absoluto n 
    | n >= 0 = n
    | n < 0 = -n

-- b
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y 
    | absoluto x > absoluto y = absoluto x
    | absoluto x < absoluto y = absoluto y
    | otherwise = absoluto x

-- c
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 a b c 
    | a > b && a > c = a
    | b > a && b > c = b 
    | c > a && c > b = c
    | a == b && b == c = a

-- d
algunoEs0 :: Float -> Float -> Bool
algunoEs0 x y 
    | x == 0 = True
    | y == 0 = True
    | otherwise = False

algunoEs0PM :: Float -> Float -> Bool
algunoEs0PM 0 _ = True
algunoEs0PM _ 0 = True
algunoEs0PM _ _ = False

-- e
ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y 
    | x == 0 && y == 0 = True
    | otherwise = False

ambosSon0PM :: Float -> Float -> Bool
ambosSon0PM 0 0 = True
ambosSon0PM _ 0 = False
ambosSon0PM 0 _ = False
ambosSon0PM _ _ = False

-- f
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y 
    | x <= 3 && y <= 3 = True
    | (x > 3 && x <= 7) && (y > 3 && y <= 7) = True
    | x >= 7 && y >= 7 = True
    | otherwise = False

-- g
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z 
    | (x == y && y == z) = x
    | x == y = x + z
    | (x == z || y == z) = x + y
    | otherwise = x + y + z

-- h
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y 
    | (abs (x) >= abs (y)) && (abs (x) `mod` abs (y) == 0) = True
    | otherwise = False

-- i
digitoUnidades :: Integer -> Integer
digitoUnidades x = rem x 10

-- j
digitoDecenas :: Integer -> Integer
digitoDecenas x = div (rem x 100) 10

-- Ej 3
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b = (a /= 0) && (b /= 0) && (esMultiploDe a b)

-- Ej 4
-- a 
prodInt :: (Float, Float) -> (Float, Float) -> Float
prodInt (x, y) (v, w) = (x * v) + (y * w)

-- b
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor (x, y) (v, w) 
    | (x < v) && (y < v) = True
    | otherwise = False

-- c
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (x, y) (v, w) = sqrt ((x - v)^2 + (y - w)^2)

-- d
sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (x, y, z) = x + y + z

-- e
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (x, y, z) a 
    | (a > 0) && (esMultiploDe (x) a) && (esMultiploDe (y) a) && (esMultiploDe (z) a) = (x) + (y) + (z)
    | (a > 0) && (esMultiploDe (x) a) && (esMultiploDe (y) a) = (x) + (y)
    | (a > 0) && (esMultiploDe (x) a) && (esMultiploDe (z) a) = (x) + (z)
    | (a > 0) && (esMultiploDe (y) a) && (esMultiploDe (z) a) = (y) + (z)
    | (a > 0) && (esMultiploDe (x) a) = x
    | (a > 0) && (esMultiploDe (y) a) = y
    | (a > 0) && (esMultiploDe (z) a) = z

-- f
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x, y, z) 
    | esMultiploDe (x) 2 = 1
    | not (esMultiploDe (x) 2) && esMultiploDe (y) 2 = 2
    | not (esMultiploDe (x) 2) && not (esMultiploDe (y) 2) && esMultiploDe (z) 2 = 3
    | not (esMultiploDe (x) 2) && not (esMultiploDe (y) 2) && not (esMultiploDe (z) 2) = 4

-- g
creaPar :: a -> b -> (a, b)
creaPar a b = (a, b)

-- h
invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)

-- Ej 5
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (x, y, z) = (f1 x > g1 x) && (f1 y > g1 y) && (f1 z > g1 z)

f1 :: Integer -> Integer
f1 x 
    | x <= 7 = x^2
    | x > 7 = (2 * x) - 1

g1 :: Integer -> Integer
g1 x = if esPar x then x `div` 2 else 3 * x + 1

esPar :: Integer -> Bool
esPar x = (x `mod` 2) == 0

-- Ej 6
bisiesto :: Integer -> Bool
bisiesto a = not (not (esMultiploDe a 4) || (esMultiploDe a 100 && not (esMultiploDe a 400)))

-- Ej 7
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (a, b, c) (x, y, z) = abs (a - x) + abs (b - y) + abs (c - z)

-- Ej 8
comparar :: Integer -> Integer -> Integer
comparar a b 
    | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
    | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
    | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = x `mod` 10 + (x `div` 10) `mod` 10