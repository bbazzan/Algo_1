import Distribution.Simple.Utils (xargs)
-- Ej 1
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- Ej 2
ultimo :: [t] -> t
ultimo [x] = x
ultimo (_:xs) = ultimo xs

