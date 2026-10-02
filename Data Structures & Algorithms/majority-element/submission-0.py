class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand, cnt = None, 0
        for num in nums:
            if cnt == 0:
                cand = num
            if cand == num:
                cnt += 1
            else:
                cnt -= 1
        return cand