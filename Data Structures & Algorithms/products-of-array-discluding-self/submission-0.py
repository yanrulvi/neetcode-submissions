class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = []
        prod = 1
        res = [0] * len(nums)

        for i, num in enumerate(nums):
            if num == 0:
                zeros.append(i)
                if len(zeros) == 2:
                    return res
                continue
            prod *= num
        
        if zeros:
            res[zeros[0]] = prod
            return res
        
        for i in range(len(nums)):
            res[i] = prod // nums[i]
        return res