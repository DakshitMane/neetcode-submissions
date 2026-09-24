class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(c.lower() for c in s if c.isalnum())
        lo, hi = 0, len(s1) - 1
        while lo < hi:
            if s1[lo] != s1[hi]:
                return False
            lo += 1
            hi -= 1
        return True