class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 3/9/26
        if len(nums)<2:
            return len(nums)

        nums.sort()

        i = 0
        cur_max = 0
        temp = 1
        while i<len(nums)-1:
            if nums[i] == nums[i+1]-1 :
                temp+=1
                i+=1
                continue
            elif nums[i]==nums[i+1]:
                i+=1
                continue
            cur_max = max(cur_max,temp)
            i+=1
            temp = 1
        cur_max = max(cur_max,temp)   
        return cur_max