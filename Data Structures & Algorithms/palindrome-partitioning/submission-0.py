class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPalindrom(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -=1
            return True
        
        def dfs(i, j):
            if j >= len(s):
                if i == j:
                    res.append(part.copy())
                return

            if isPalindrom(s, i, j):
                part.append(s[i: j + 1])
                dfs(j + 1, j + 1)
                part.pop()
            
            dfs(i, j + 1)

        dfs(0, 0)
        return res