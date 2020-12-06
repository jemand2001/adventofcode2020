module Main where

import Data.List.Split (splitOn)

joinLines :: [String] -> [String]
joinLines [] = []
joinLines ("" : xs) = joinLines xs
joinLines xs
    | all null xs = []
    | otherwise = concat (" ":takeWhile (not . null) xs)
                : joinLines (dropWhile (not . null) xs)

required :: [String]
required = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
    -- "cid"
    ]

isValidA :: String -> Bool
isValidA line = all (`elem` [key | (key:_) <- map (splitOn ":") $ words line]) required

main :: IO ()
main = interact $ show . length . filter isValidA . joinLines . lines
