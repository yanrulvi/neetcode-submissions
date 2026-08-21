class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k + 1
        heapq.heapify(nums)
        for _ in range(k):
            res = heapq.heappop(nums)
        return res