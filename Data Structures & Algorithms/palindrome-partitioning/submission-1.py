class Solution:
    def partition(self, s: str) -> List[List[str]]:
        size = len(s)
        op = []

        def backtrack(index,path):
            if index == size:
                if path[-1]==path[-1][::-1]:
                    op.append(path.copy())
                return

            cur = s[index]
            
            if path[-1] == path[-1][::-1]:
                path.append(cur)            
                backtrack(index+1,path)
                path.pop()

            path[-1] = path[-1]+cur
            backtrack(index+1,path.copy())

        backtrack(1,[s[0]]) 
        return op           