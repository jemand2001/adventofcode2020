module Main where

findNumbersA :: [Integer] -> Integer
findNumbersA xs = head [a * b | a <- xs, b <- xs, a + b == 2020]

findNumbersB :: [Integer] -> Integer
findNumbersB xs = head [a * b * c | a <- xs, b <- xs, c <- xs, a + b + c == 2020]

main :: IO ()
main = interact $ (++"\n") . show . findNumbersB . map read . words
