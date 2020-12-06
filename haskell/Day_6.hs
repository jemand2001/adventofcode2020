module Main where

joinLines :: [String] -> [String]
joinLines [] = []
joinLines ("" : xs) = joinLines xs
joinLines xs = unlines (takeWhile (not . null) xs) : joinLines (dropWhile (not . null) xs)

replace :: Eq a => a -> a -> [a] -> [a]
replace a b = map (\x -> if x == a then b else x)

unique :: Eq a => [a] -> [a] -- O(n^2)
unique [] = []
unique (x:xs)-- = filter (/= x) $ unique xs
   | x `elem` xs = unique xs
   | otherwise = x : unique xs
-- unique = foldr (\x -> filter (/= x)) []

union :: Eq a => [[a]] -> [a]
union = unique . concat

intersection :: Eq a => [[a]] -> [a]
intersection [] = []
intersection (l:ls) = filter (\x -> all (elem x) ls) l

intersectionA :: Eq a => [a] -> [a] -> [a]
intersectionA s1 s2 = unique [x | x <- s1, x `elem` s2]

main :: IO ()
main = interact $ (++ "\n") . show . sum . map (length . union . words) . joinLines . lines

groupA :: String
groupA = "dzapkcqlmbsrivuxhg\nbazpqwldgvmxkuchsr\nqgxzlhkpmbvrcdasu\nlghvqradxukpsbcmz"

groupB :: String
groupB = "lxn\nrkq\ndcb\na"

groups :: String
groups = groupA ++ "\n\n" ++ groupB
