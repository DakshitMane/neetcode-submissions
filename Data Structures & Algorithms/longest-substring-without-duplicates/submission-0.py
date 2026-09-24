class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        lo, maxLength = 0, 0
        for hi in range(len(s)):
            while s[hi] in sett:
                sett.remove(s[lo])
                lo += 1
            sett.add(s[hi])
            maxLength = max(maxLength, (hi - lo + 1))
        return maxLength