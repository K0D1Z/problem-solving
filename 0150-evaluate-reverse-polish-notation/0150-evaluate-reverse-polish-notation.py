class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        op = ['+', '-', '/', '*']
        
        for t in tokens:
            if t in op:
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    res = a + b
                elif t == '-':
                    res = a - b
                elif t == '/':
                    res = int(a / b)
                else:
                    res = a * b
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[0]