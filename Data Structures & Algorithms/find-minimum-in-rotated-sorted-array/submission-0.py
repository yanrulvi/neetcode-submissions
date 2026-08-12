class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("inf")
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (right + left) // 2
            res = min(res, nums[middle])
            if nums[left] > nums[middle]:
                right = middle - 1
            elif nums[right] < nums[middle]:
                left = middle + 1
            else:
                res = min(res, nums[left])
                break
        return res