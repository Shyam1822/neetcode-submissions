class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 16/9/26
        # 
        op = []
        size = len(nums)
        nums.sort()

        def backtrack(index,path):
            if index==size:
                if path not in op:
                    op.append(path.copy())
                return
            
            for i in range(index,size):
                path.append(nums[i])
                # print(path,op)
                if path not in op:
                    op.append(path.copy())
                backtrack(i+1,path)
                path.pop()
                backtrack(i+1,path)
            # print(op)
        
        backtrack(0,[])
        return op
        
            
                
                
