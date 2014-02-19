--[[
Problem 7: 10001st Prime

 *can't use Sieve of Erastothenes since we dont have a defined limit, dont know
 where will the 10001st will end up
 *will be using the trial division but will limit only to primes below the square root 
 of the candidate to slightly increase efficiency

--]]

local primeMax = 10001
local primeList = {2 , 3}
-- i dont know how much penalty it is using # operator of lua, so on safe side just track the count
local primeCount = #primeList


local function isPrime ( candidate ) 
   sqrt = candidate ^ 0.5
   for i = 1, primeCount do
        if primeList[i] > sqrt then return true end
        if candidate % primeList[i] == 0 then return false end
   end
   return true
end
n = primeList[primeCount] + 1 -- start off with the list we already have

while primeCount < primeMax do
    if isPrime(n) then
        primeCount = primeCount + 1
        print("Found "..primeCount.."st: "..n)
        primeList[primeCount] = n
    end
    n = n + 1
end
