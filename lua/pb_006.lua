--[[
Problem 6: Sum square difference
The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first 
        ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one 
        hundred natural numbers and the square of the sum.

--]]

local kLimit = 100 

local function getSquareOfSum( pMax)
    local sum = 0
    for i = 1, pMax do
       sum = sum + i
    end
    return sum ^ 2
end

local function getSumOfSquares ( pMax )
    local sum = 0
    for i = 1, pMax do
        sum = sum + i ^ 2
    end
    return sum
end


print("Sum square difference : "..(getSquareOfSum(kLimit)-getSumOfSquares(kLimit)))


