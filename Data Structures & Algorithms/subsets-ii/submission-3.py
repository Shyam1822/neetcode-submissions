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
            
            # print(path,op)
            
            path.append(nums[index])
            backtrack(index+1,path)
            path.pop()
            while index+1<size and nums[index]==nums[index+1]:
                index+=1
            backtrack(index+1,path)
            # print(op)
        
        backtrack(0,[])
        return op
        
            
                
                
