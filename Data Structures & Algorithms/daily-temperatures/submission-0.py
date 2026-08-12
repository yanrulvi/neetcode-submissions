class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                tem_from_stack = stack.pop()
                res[tem_from_stack[0]] = i - tem_from_stack[0]
            stack.append([i, t])
        return res