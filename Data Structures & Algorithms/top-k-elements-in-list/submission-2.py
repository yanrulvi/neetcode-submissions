class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        freq_arr = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            freq[num] += 1
        for val, cnt in freq.items():
            freq_arr[cnt].append(val)
        
        for i in range(len(freq_arr) - 1, 0, -1):
            for num in freq_arr[i]:
                res.append(num)
        return res[:k]