class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #6/9/26 
        op=[]
        nums.sort()
        size = len(nums)

        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l,r = i+1,size-1
            while l<r:
                l_ele,r_ele = nums[l],nums[r]
                sum_t = l_ele+r_ele
                if sum_t==target:
                    curr = sorted([l_ele,-target,r_ele])
                    if curr not in op:
                        op.append(curr)
                        l+=1
                        r-=1
                        continue
                if -sum_t<-target:
                    r-=1
                    continue
                l+=1
        return op