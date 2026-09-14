class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(sub, i):
            nonlocal res

            if i >= len(digits):
                res.append("".join(sub))
                return
            
            for ch in d[digits[i]]:
                sub.append(ch)
                dfs(sub, i + 1)
                sub.pop()

        dfs([], 0)
        return res