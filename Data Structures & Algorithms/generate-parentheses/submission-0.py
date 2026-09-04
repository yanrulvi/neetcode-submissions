class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(str_, opened, closed):
            nonlocal res

            if opened == n:
                str_ = str_ + ')' * (n - closed)
                res.append(str_)
                return
            
            dfs(str_ + '(', opened + 1, closed)
            if closed < opened:
                dfs(str_ + ')', opened, closed + 1)

        dfs("", 0, 0)
        return res