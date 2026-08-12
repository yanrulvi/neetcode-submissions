class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            if token in ops:
                el1 = stack.pop()
                el2 = stack.pop()
                if token == "+":
                    stack.append(el1 + el2)
                elif token == "-":
                    stack.append(el2 - el1)
                elif token == "*":
                    stack.append(el1 * el2)
                elif token == "/":
                    stack.append(int(float(el2) / el1))
        
        return stack[-1]