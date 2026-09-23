class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 23/9/26

        nums.sort()
        size = len(nums)
        op = []

        def backtrack(index,cur,cur_sum):
            if cur_sum==target:
                op.append(cur.copy())
                return
            
            if cur_sum>target or index >= size:
                return
            
            val = nums[index]
            cur.append(val)
            backtrack(index,cur,cur_sum+val)
            cur.pop()

            backtrack(index+1,cur,cur_sum)

        backtrack(0,[],0)
        return op
                
