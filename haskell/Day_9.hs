module Main where

findInvalid :: [Integer] -> Integer
findInvalid [] = -1
findInvalid (x:xs)
    | number `notElem` [a + b | a <- preamble, b <- preamble, a /= b] = number
    | otherwise = findInvalid xs
    where
        preamble = take 25 (x:xs)
        number = xs !! 24

main :: IO ()
main = interact $ (++ "\n") . show . findInvalid . map read . lines
