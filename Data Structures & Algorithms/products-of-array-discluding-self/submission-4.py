class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        if len(nums)==1:
            return nums
        prefix = [1]
        suffix = [1]
        ps,ss = 1,1
        for i in range(1,len(nums)):
            # ps *= 
            # print(ps)
            prefix.append(nums[i-1]*prefix[i-1])

        for i in range(1,len(nums)):
            # ss *= nums[-i]
            # print(nums[-i])
            suffix.append(nums[-i]*suffix[i-1])

        suffix = suffix[::-1]
        # print(prefix,suffix)

        op = []
        for i in range(len(nums)):
            op.append(prefix[i]*suffix[i])
        return op