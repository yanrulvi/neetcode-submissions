class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if len(s2) < k:
            return False
            
        count = Counter(s1)

        for i in range(k):
            count[s2[i]] = count.get(s2[i], 0) - 1
            if count[s2[i]] == 0:
                del count[s2[i]]
        
        for i in range(k, len(s2)):
            if not count:
                return True

            count[s2[i]] = count.get(s2[i], 0) - 1
            if count[s2[i]] == 0:
                del count[s2[i]]
            count[s2[i - k]] = count.get(s2[i - k], 0) + 1
            if count[s2[i - k]] == 0:
                del count[s2[i - k]]

        return not count