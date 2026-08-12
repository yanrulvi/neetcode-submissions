class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []

        for num in nums:
            freq[num] += 1
        freq = freq.items()
        freq = sorted(freq, key=lambda x: -x[1])
        for i in range(k):
            res.append(freq[i][0])
        return res