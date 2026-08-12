class Solution:
    def f(self, piles: List[int], h: int, k: int) -> bool:
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k
        return hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            m = (left + right) // 2
            if self.f(piles, h, m):
                right = m - 1
            else:
                left = m + 1

        return left