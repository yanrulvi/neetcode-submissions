class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []
        for ch in s:
            if ch in bracket_pairs.keys():
                stack.append(ch)
            elif ch in bracket_pairs.values():
                if not stack or ch != bracket_pairs[stack.pop()]:
                    return False
        if stack:
            return False
        return True