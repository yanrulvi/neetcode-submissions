class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        res = 0
        for j in range(len(s)):
            if i >= len(g):
                return res
            if g[i] - s[j] <= 0:
                res += 1
                i += 1
        return res