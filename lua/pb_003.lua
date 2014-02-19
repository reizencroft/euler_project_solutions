
-- local kTargetNumber = 600851475143
local kTargetNumber = 600851475143
local primes = { 1 }
local nonPrimes = { }

local function testIfPrime ( pTestee )
    
end

-- get all prime numbers from 0 to pMaxNumber using the Sieve of Eratosthenes
local function getAllPrimes ( pMaxNumber)
    print("Get all primes for "..pMaxNumber)
    for i = 1, pMaxNumber do
        nonPrimes[i] = 0
    end

    k = 2 -- factor
    while ( k < pMaxNumber) do
        -- print(k)
        primes[#primes+1] = k
        p = k
        while ( p < pMaxNumber ) do
           p = p + k
           nonPrimes[p] = 1
        end
        k = k + 1
        while ( nonPrimes[k] ~= 0 ) and ( k < pMaxNumber) do
            k = k + 1
        end
        print("found "..k)
    end
 --    for i = 1, pMaxNumber do
 --        print (i.."=>"..nonPrimes[i])
 --    end
end


getAllPrimes ( kTargetNumber ^ 0.5)
-- then test which primes are a factor of target
print("factors of "..kTargetNumber..":" )
for i = 1, #primes do
    if( kTargetNumber % primes[i] == 0 ) then
        print(primes[i])
    end
end


