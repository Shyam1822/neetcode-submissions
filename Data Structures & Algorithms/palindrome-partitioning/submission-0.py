class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #21/9/26
        
        op = []
        size = len(s)

        def backtrack(i,path):
            if i==size: 
                # print(path)
                if path[-1]==path[-1][::-1]:
                    op.append(path.copy())
                    # print(op)
                return
            
            if path[-1]==path[-1][::-1]:
                path.append(s[i])
                backtrack(i+1,path)
                path.pop()
            

            path[-1] = path[-1]+s[i]
            backtrack(i+1,path.copy())
        
        backtrack(1,[s[0]])
        return op