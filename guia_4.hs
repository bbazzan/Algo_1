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
todosDigitosIguales n 
    | n < 10 = True
    | otherwise = (n `mod ` 10) == (n `div` 10) `mod` 10 && todosDigitosIguales (n `div` 10)

-- Ej 8
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i = (n `div` 10 ^ (cantDigitos n - i)) `mod` 10

cantDigitos :: Integer -> Integer
cantDigitos n 
    | n < 10 = 1
    | otherwise  = 1 + cantDigitos (n `div` 10)

-- Ej 9
esCapicua :: Integer -> Bool
esCapicua n 
    | cantDigitos n == 1 = True
    | cantDigitos n == 2 || cantDigitos n == 3 = iesimoDigito n 1 == (n `mod` 10)
    | otherwise = iesimoDigito n 1 == (n `mod` 10) && esCapicua (div (mod n (10 ^ ((cantDigitos n) - 1))) 10)

-- Ej 10
-- a
f1 :: Integer -> Integer
f1 0 = 1
f1 n = 2 ^ n + f1 (n - 1)

-- b
f2 :: Float -> Integer -> Float
f2 q 1 = q
f2 q n = q ^ n + f2 q (n - 1)

-- c
f3 :: Float -> Integer -> Float
f3 q 1 = q ^ 2 + q
f3 q n = q ^ (2 * n) + q ^ ((2 * n) - 1) + f3 q (n - 1)

-- d
f4 :: Float -> Integer -> Float
f4 q 0 = 1
f4 q n = f3 q n - f2 q (n - 1)  -- suma de n a 2n = suma de 0 a 2n - suma de 0 n-1

-- Ej 11
-- a
eAprox :: Integer -> Float
eAprox 0 = 1
eAprox n = (1.0 / fromIntegral (factorial n)) + eAprox (n - 1)

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- b
e :: Float
e = eAprox 10

-- Ej 12
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = (sucesion n) - 1

sucesion :: Integer -> Float
sucesion 1 = 2
sucesion n = 2 + (1 / sucesion (n - 1))

-- Ej 13
dobleSumatoria :: Integer -> Integer -> Integer
dobleSumatoria 1 m = sumatoriaSobreM 1 m
dobleSumatoria n m = sumatoriaSobreM n m + dobleSumatoria (n - 1) m

sumatoriaSobreM :: Integer -> Integer -> Integer
sumatoriaSobreM n 1 = n
sumatoriaSobreM n m = (n ^ m) + sumatoriaSobreM n (m - 1)

-- Ej 14
sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias _ 0 _ = 0
sumaPotencias q n m = sumaPotencias q (n - 1) m + sumatoriaInternaPot q n m

sumatoriaInternaPot :: Integer -> Integer -> Integer -> Integer
sumatoriaInternaPot _ _ 0 = 0
sumatoriaInternaPot i j k = i ^ (j + k) + sumatoriaInternaPot i j (k - 1)

-- Ej 15
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 1 m = sumaRacionalesAux 1 m
sumaRacionales n m = sumaRacionalesAux n m + sumaRacionales (n - 1) m

sumaRacionalesAux :: Integer -> Integer -> Float
sumaRacionalesAux n 1 = fromIntegral n
sumaRacionalesAux n m = ((fromIntegral n) / (fromIntegral m)) + sumaRacionalesAux n (m - 1)

-- Ej 16
-- a
menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorAux n 2

menorDivisorAux :: Integer -> Integer -> Integer
menorDivisorAux n i 
    | n `mod` i == 0 = i
    | otherwise = menorDivisorAux n (i + 1)

-- b
esPrimo :: Integer -> Bool
esPrimo n 
    | menorDivisor n == n = True
    | otherwise = False

-- c
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos a b = maxComunDenom a b == 1

maxComunDenom :: Integer -> Integer -> Integer
maxComunDenom a 0 = a
maxComunDenom a b = maxComunDenom b (a `mod` b)

-- d
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = nEsimoPrimoAux n 2

nEsimoPrimoAux :: Integer -> Integer -> Integer
nEsimoPrimoAux n i 
    | esPrimo i && n == 1 = i
    | esPrimo i = nEsimoPrimoAux (n - 1) (i + 1)
    | otherwise = nEsimoPrimoAux n (i + 1)