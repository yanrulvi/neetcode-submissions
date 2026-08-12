class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        count = Counter(s1)
        count2 = Counter(s2[:k])
        res = count == count2

        for right in range(k, len(s2)):
            if res: return res
            count2[s2[right]] = count2.get(s2[right], 0) + 1
            count2[s2[right - k]] -= 1
            if count2[s2[right - k]] == 0:
                del count2[s2[right - k]]
            res = count == count2

        return res