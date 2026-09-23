class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 23/9/26

        nums.sort()
        size = len(nums)
        op = []

        def backtrack(index,cur):
            if sum(cur)==target:
                op.append(cur.copy())
                return
            
            if sum(cur)>target or index >= size:
                return
            
            cur.append(nums[index])
            backtrack(index,cur)
            cur.pop()

            backtrack(index+1,cur)

        backtrack(0,[])
        return op
                
