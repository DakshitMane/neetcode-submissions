class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k: int)-> bool:
            hours = 0
            for pile in piles:
                hours += pile // k
                if pile % k != 0:
                    hours += 1
                if hours > h:
                    return False
            return True
        
        lo, hi = 1, max(piles)
        ans = hi
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if canEat(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans