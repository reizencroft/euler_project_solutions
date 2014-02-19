

local kMaxFibonacciTermValue = 4000000

local function getNextFibTerm( pA, pB)

end


local function getSumOfEvenFibTerm( pMax )
    local sum = 0
    local a = 0
    local b = 1

    while ( b < pMax ) do
        local c = b
        b = a + b
        a = c
        if ( b % 2 == 0 ) then
           sum = sum + b
        end
    end

    return sum
end

print (getSumOfEvenFibTerm ( kMaxFibonacciTermValue ))

