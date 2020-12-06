module Main where

import Data.List.Split ( splitOn )

xor :: Bool -> Bool -> Bool
xor a b = a /= b

countLetter :: String -> Char -> Int
countLetter str c = length $ filter (== c) str

isValidA :: [String] -> Bool
isValidA [c, [l, ':'], p] = low <= count && high >= count
    where 
        [low, high] = map read $ splitOn "-" c :: [Int]
        count = countLetter p l

countValidA :: [[String]] -> Int
countValidA = length . filter isValidA

isValidB :: [String] -> Bool
isValidB [c, [l, ':'], p] = (p !! (pos1-1) == l) `xor` (p !! (pos2 - 1) == l)
    where [pos1, pos2] = map read $ splitOn "-" c :: [Int]

countValidB :: [[String]] -> Int
countValidB = length . filter isValidB

main :: IO ()
main = interact $ (++"\n") . show . countValidB . filter (not . null) . map words . lines
