class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])

        for i in tokens:
            if i.isdigit() or len(i)>1:
                stack.append(i)
                continue
            
            b,a = int(stack.pop()),int(stack.pop())

            if i == '+':
                stack.append(a+b)
            elif i == '-':
                stack.append(a-b)
            elif i == '*':
                stack.append(a*b)
            elif i == "/":
                stack.append(int(a/b))
        return stack[0]