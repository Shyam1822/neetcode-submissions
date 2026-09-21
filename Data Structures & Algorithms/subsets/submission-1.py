class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # also makes sense to search via dfs, try next time

        nums.sort()

        op = []

        s = len(nums)

        def backtrack(i,path):
            if i==s:
                op.append(path.copy())
                return
            
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()
            backtrack(i+1,path)
        
        backtrack(0,[])
        return op