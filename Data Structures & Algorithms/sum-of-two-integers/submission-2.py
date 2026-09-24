class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK, BIT_MASK = 0xFFFFFFFF, 0x7FFFFFFF
        while b != 0:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry
        return a if a <= BIT_MASK else ~(a ^ MASK)