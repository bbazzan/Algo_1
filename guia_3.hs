-- Problema 1
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

-- Problema 2
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
    | x == y && y == z = x
    | x == y = x + z
    | x == z || y == z = x + y
    | otherwise = x + y + z

-- h
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y 
    | x < 0 || y < 0 = False
    | x > y && mod x y == 0 = True
    | otherwise = False

-- i
digitoUnidades :: Integer -> Integer
digitoUnidades x = rem x 10

-- j
digitoDecenas :: Integer -> Integer
digitoDecenas x = div (rem x 100) 10