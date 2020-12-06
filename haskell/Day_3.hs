module Main where

countTrees :: (Int, Int) -> [String] -> Int
countTrees _ [] = 0
countTrees (x, y) ((spot:_):forest)
    | spot == '#' = 1 + rest
    | otherwise = rest
    where rest = countTrees (x, y) $ map (drop x) forest

main :: IO ()
main = interact $ show . countTrees (3, 1) . lines
