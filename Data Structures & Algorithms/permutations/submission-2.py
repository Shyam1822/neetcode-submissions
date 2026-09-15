class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        op = []
        size = len(nums)
        boolean_array = [False for _ in range(size)]
        i = 0
        def backtrack(path):
            # base condition
            # print(path)
            if len(path)==len(nums):
                op.append(path.copy())
                return
            for i in range(size):
                # print(path,boolean_array)
                if not boolean_array[i]:
                    boolean_array[i]=True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    boolean_array[i]=False
        backtrack([])
        return op
                
            
            
