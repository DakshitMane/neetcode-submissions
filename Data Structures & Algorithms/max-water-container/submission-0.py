class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo, hi = 0, len(heights) - 1
        maxArea = 0
        while lo <= hi:
            currArea = min(heights[lo], heights[hi]) * abs(hi - lo)
            maxArea = max(maxArea, currArea)
            if heights[lo] <= heights[hi]:
                lo += 1
            else:
                hi -= 1
        return maxArea