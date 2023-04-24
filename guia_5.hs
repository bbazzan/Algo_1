import Distribution.Simple.Utils (xargs)
-- Ej 1
-- a
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- b
ultimo :: [t] -> t
ultimo [x] = x
ultimo (_:xs) = ultimo xs

-- c
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

-- d
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]