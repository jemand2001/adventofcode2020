module Main where

execute1 :: String -> Integer -> Integer -> Integer -> (Integer, Integer)
execute1 "acc" ip acc arg = (arg + acc, succ ip)
execute1 "nop" ip acc _ = (acc, succ ip)
execute1 "jmp" ip acc arg = (acc, ip + arg)

execute :: [(String, Integer)] -> Integer -> Integer -> Integer
execute instructions ip acc = 
