class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #27/8/26

        return len(nums)!=len(set(nums))