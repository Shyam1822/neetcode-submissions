class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        op = []

        def check(s):
            # print(s)
            open = 0
            for i in s:
                open+=1 if i=='(' else -1
                if open<0:
                    return False
            return not open
        
        def rec(s):
            if ((s.count('(')>n) or (s.count(')')>n)):
                # print(s)
                return

            if n * 2 == len(s):
                if check(s):
                    op.append(s)
                return
            
            rec(s+'(')
            rec(s+')')

        rec("")
        return op
