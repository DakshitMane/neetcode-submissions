class Solution:
    def trap(self, height: List[int]) -> int:
        lo, hi, res = 0, len(height) - 1, 0
        lmax, rmax = 0, 0
        while lo < hi:
            if height[lo] < height[hi]:
                lmax = max(lmax, height[lo])
                res += lmax - height[lo]
                lo += 1
            else:
                rmax = max(rmax, height[hi])
                res += rmax - height[hi]
                hi -= 1
        return res