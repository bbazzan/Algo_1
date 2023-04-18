import Distribution.Simple.Setup (showBuildInfoCommand)
-- Ej 1
fibonacci :: Integer -> Integer
fibonacci 0 = 1
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)

-- Ej 2
parteEntera :: Float -> Integer
parteEntera n 
    | n < 1 = 0
    | otherwise = 1 + parteEntera (n - 1)

-- Ej 3
esDivisible :: Integer -> Integer -> Bool
esDivisible a b 
    | a < b = False
    | a == b = True
    | otherwise = esDivisible (a - b) b

-- Ej 4
sumaImpares :: Integer -> Integer
sumaImpares 1 = 1
sumaImpares n = n_esimoImpar + sumaImpares (n -1) where n_esimoImpar = 2 * n - 1

-- Ej 5
medioFactorial :: Integer -> Integer
medioFactorial 0 = 1
medioFactorial 1 = 1
medioFactorial 2 = 2
medioFactorial 3 = 3
medioFactorial n = n * medioFactorial (n - 2)

-- Ej 6
sumaDigitos :: Integer -> Integer
sumaDigitos n 
    | n `div` 10 == 0 = n
    | (n `div` 10) > 0 && (n `div` 10) <= 9 = n `div` 10 + n `mod` 10
    | otherwise = n `mod` 10 + sumaDigitos(n `div` 10)

-- Ej 7
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n = 

-- allEqualDigits :: Int -> Bool
-- allEqualDigits n = go (n `div` 10) (n `mod` 10)
--   where
--     go 0 _ = True
--     go n lastDigit
--       | n `mod` 10 == lastDigit = go (n `div` 10) lastDigit
--       | otherwise = False