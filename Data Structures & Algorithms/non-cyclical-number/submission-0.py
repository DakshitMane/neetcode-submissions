class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n: int)-> int:
            sumDigit = 0
            while n > 0:
                digit = n % 10
                digit = digit ** 2
                sumDigit += digit
                n //= 10
            return sumDigit
        
        sett = set()
        while n not in sett:
            sett.add(n)
            n = sumOfSquares(n)
            if n == 1:
                return True 
        return False