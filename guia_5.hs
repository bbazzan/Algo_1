import Distribution.Simple.Utils (xargs)
import Language.Haskell.TH (Lit(IntegerL), nameBase)
import Data.Map.Internal.Debug (ordered)
-- Ej 1
-- a
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- b
ultimo :: [t] -> t
ultimo [] = undefined
ultimo [x] = x
ultimo (_:xs) = ultimo xs

-- c
principio :: [t] -> [t]
principio [] = []
principio [x] = []
principio (x:xs) = x : principio xs

-- d
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]

-- Ej 2
-- a
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece y (x:xs) 
    | y == x = True
    | otherwise = pertenece y xs

-- b
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [_] = True
todosIguales (x:y:xs) = x == y && todosIguales (y:xs)

-- c
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) = not (pertenece x xs) && todosDistintos xs

-- d
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) = pertenece x xs || hayRepetidos xs

-- e
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar y (x:xs) 
    | y == x = xs
    | otherwise = x : quitar y xs

-- f
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos y (x:xs) 
    | y == x = quitarTodos y xs
    | otherwise = x : quitarTodos y xs

-- g
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : eliminarRepetidos (quitarTodos x xs)

-- h
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos xs ys = todosPertenecen (eliminarRepetidos xs) (eliminarRepetidos ys) && todosPertenecen (eliminarRepetidos ys) (eliminarRepetidos xs)

todosPertenecen :: (Eq t) => [t] -> [t] -> Bool
todosPertenecen [] _ = True
todosPertenecen (x:xs) ys = pertenece x ys && todosPertenecen xs ys

-- i
capicua :: (Eq t) => [t] -> Bool
capicua xs = xs == reverso xs

-- Ej 3
-- a
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- b
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs

-- c
maximo :: [Integer] -> Integer
maximo [] = undefined
maximo [x] = x
maximo (x:xs) = maximoEntreDos x (maximo xs)

maximoEntreDos :: Integer -> Integer -> Integer
maximoEntreDos x y = if x > y then x else y

-- d
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = (n + x) : sumarN n xs

-- e
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- f
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo xs = sumarN (ultimo xs) xs

-- g
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) 
    | esPar x = x : pares xs
    | otherwise = pares xs

esPar :: Integer -> Bool
esPar x = x `mod` 2 == 0

-- h
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) 
    | esMultiploDe x n = x : multiplosDeN n xs
    | otherwise = multiplosDeN n xs

esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y 
    | (abs (x) >= abs (y)) && (abs (x) `mod` abs (y) == 0) = True
    | otherwise = False

-- i
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar (x:xs) = insertar x (ordenar xs)

insertar :: Integer -> [Integer] -> [Integer]
insertar x [] = [x]
insertar x (y:ys) 
    | x <= y = x : y : ys
    | otherwise = y : insertar x ys
 
-- Ej 4
-- a
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) 
    | x == ' ' && y == ' ' = sacarBlancosRepetidos (y:xs)
    | otherwise = x : sacarBlancosRepetidos (y:xs)

-- b
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras xs = contarPalabrasAux (sacarBlancosRepetidos xs) 0 False

contarPalabrasAux :: [Char] -> Integer -> Bool -> Integer
contarPalabrasAux [] cuenta _ = cuenta
contarPalabrasAux (x:xs) cuenta enPalabra 
    | x == ' ' = contarPalabrasAux xs cuenta False
    | not enPalabra = contarPalabrasAux xs (cuenta + 1) True
    | otherwise = contarPalabrasAux xs cuenta True

-- c 
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga xs = auxPML (sacarBlancosRepetidos xs) [] []
    where
        auxPML [] actual masLarga = if longitud actual > longitud masLarga then actual else masLarga
        auxPML (x:xs) actual masLarga 
            | x == ' ' = auxPML xs [] (if longitud actual > longitud masLarga then actual else masLarga)
            | otherwise = auxPML xs (actual ++ [x]) masLarga

-- d
palabras :: [Char] -> [[Char]]
palabras xs = auxPalabras (sacarBlancosRepetidos xs) [] []
    where 
        auxPalabras [] actual resultado = if null actual then resultado else resultado ++ [actual]
        auxPalabras (x:xs) actual resultado 
            | x == ' ' = auxPalabras xs [] (if null actual then resultado else resultado ++ [actual])
            | otherwise = auxPalabras xs (actual ++ [x]) resultado

-- e
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs

-- f
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos [x] = x
aplanarConBlancos (x:xs) = x ++ " " ++ aplanarConBlancos xs

-- g
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos [x] n = x
aplanarConNBlancos (x:xs) n = x ++ replicar n ' ' ++ aplanarConNBlancos xs n 
    where 
        replicar 0 _ = []
        replicar m c = c : replicar (m-1) c

-- Ej 5
-- a
nat2bin :: Integer -> [Integer]
nat2bin 0 = [0]
nat2bin n = reverse (auxiliar n) 
    where 
        auxiliar 0 = []
        auxiliar n = (n `mod` 2) : auxiliar (n `div` 2)

-- b
bin2nat :: [Integer] -> Integer
bin2nat [] = 0
bin2nat (x:xs) = x * 2 ^ longitud xs + bin2nat xs

-- c
nat2hex :: Int -> [Char]
nat2hex n 
    | n < 16 = [nat2digito n]
    | otherwise = nat2hex (n `div` 16) ++ [nat2digito (n `mod` 16)]
    where nat2digito x = "0123456789ABCDEF" !! x

-- d
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada xs = sumaAcumuladaAux 0 xs
    where sumaAcumuladaAux _ [] = []
          sumaAcumuladaAux c (x:xs) = (c + x) : sumaAcumuladaAux (c + x) xs

-- e
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = factorizar x : descomponerEnPrimos xs

factorizar :: Integer -> [Integer]
factorizar n 
    | n <= 1 = []
    | otherwise = factorPrimoMasPequeño n : factorizar (n `div` factorPrimoMasPequeño n)
    where factorPrimoMasPequeño n = head [x | x <- [2..n], n `mod` x == 0]