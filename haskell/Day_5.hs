module Main where

replace :: Char -> Char -> String -> String
replace _ _ "" = ""
replace c1 c2 (c : s)
  | c == c1 = c2 : replace c1 c2 s
  | otherwise = c : replace c1 c2 s

replaceAll :: [Char] -> [Char] -> String -> String
replaceAll [] [] s = s
replaceAll (c1 : inp) (c2 : out) s = replaceAll inp out $ replace c1 c2 s

maxL :: Integral a => [a] -> a
maxL [x] = x
maxL (a : l) = max a $ maxL l

digitToInt :: Char -> Int
digitToInt = subtract (fromEnum '0') . fromEnum

readInt :: String -> Int
readInt = foldl (\a x -> a * 2 + digitToInt x) 0

findId :: [Int] -> Int
findId l = head [x + 1 | x <- l, x + 1 `notElem` l, x + 2 `elem` l]

main :: IO ()
-- part 1
-- main = interact $ show . maxL . map (readInt . replaceAll "BFRL" "1010") . words
-- part 2
main = interact $ show . findId . map (readInt . replaceAll "BFRL" "1010") . words
