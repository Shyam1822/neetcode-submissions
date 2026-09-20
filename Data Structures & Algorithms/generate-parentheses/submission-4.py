class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 20/9/26

        op = []

        def backtrack(path):
            
            if (path.count(')')>path.count('(')) or (path.count('(')>n):
                return
            
            if len(path)==n*2:
                op.append(path)
                return

            
            path+='('
            backtrack(path)
            path = path[:-1]
            path+=')'
            backtrack(path)
        
        backtrack('')
        return op


        

