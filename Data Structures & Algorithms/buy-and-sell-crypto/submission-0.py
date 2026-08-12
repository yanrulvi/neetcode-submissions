class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        best_diff = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                best_diff = max(best_diff, diff)
            else:
                l = r
            r += 1
        return best_diff
