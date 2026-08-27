class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #27/8/26
        index = {}

        for idx,num in enumerate(nums):
            index[num] = idx
        
        for idx,num in enumerate(nums):
            diff = target - num
            if diff in index and index[diff]!=idx:
                return[idx,index[diff]]
        return []
