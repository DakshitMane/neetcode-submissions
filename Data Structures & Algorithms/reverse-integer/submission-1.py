class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        n, rev = abs(x), 0
        while n > 0:
            rev = rev * 10 + (n % 10)
            n //= 10
        res = -rev if x < 0 else rev
        return res if (INT_MIN <= res <= INT_MAX) else 0