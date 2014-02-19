
local function isPalindrome ( pTestee )
    digits = 0
    number = pTestee
    while true do
        number = number / 10
        digits = digits + 1
        if ( math.floor(number) == 0 ) then
            break
        end
    end
    
    isPalindromic = true
    k = 1
    j = digits

    while ( k ~= j) and (j > k) do
        front = math.floor((pTestee / ( 10 ^ (j - 1)) )% 10)
        back = math.floor((pTestee / ( 10 ^ (k - 1))) % 10)
        if(front ~= back) then
            return false
        end
        k = k + 1
        j = j - 1
    end

    return isPalindromic
end


local factorA = 999
local factorB = 999
local curHighestPalindrome = -1

while factorA > 99 do
    while factorB > 99 do
       testPalindrome = factorA * factorB
       if(isPalindrome(testPalindrome)) and
           (testPalindrome > curHighestPalindrome) then
           curHighestPalindrome = testPalindrome
       end
       factorB = factorB - 1
    end
    factorA = factorA - 1
    print(factorA)
    factorB = factorA
end

print(curHighestPalindrome)
