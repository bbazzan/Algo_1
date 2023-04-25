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