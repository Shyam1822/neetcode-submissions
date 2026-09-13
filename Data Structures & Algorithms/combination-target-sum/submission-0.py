class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        op = []
        nums.sort()
        def backtrack(index,path,current_sum):
            # base condition
            if current_sum == target:
                op.append(path.copy())
                return
            if current_sum > target or index >= len(nums):
                return
            
            # print(path,index)
            path.append(nums[index])
            backtrack(index, path, current_sum+nums[index])
            path.pop()

            backtrack(index+1, path, current_sum)
                
        
        backtrack(0,[],0)
        return op

            


            
            

        
        
            

