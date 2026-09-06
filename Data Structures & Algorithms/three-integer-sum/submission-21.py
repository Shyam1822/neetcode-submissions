class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        op=[]
        # i,j=0,len(nums)-1
        # op = []
        # print(nums)
        # while i<j:
        #     print(i,j)
        #     target = 0-nums[i]-nums[j]
        #     # print(target,nums[i+1:j]+nums[j+1:])
        #     arr = [nums[i],nums[j],target]
        #     arr.sort()
        #     if ((target in nums[i+1:j]) and (arr not in op)):
        #         op.append(arr)
        #         print(op)
        #     if target < 0:
        #         j-=1
        #     elif target>0:
        #         i+=1
        #     else:
        #         if (abs(0-nums[i]+nums[j-1])<abs(0-nums[i+1]+nums[j])):
        #             i+=1
        #         # elif (abs(0-nums[i]+nums[j-1])>abs(0-nums[i+1]+nums[j])):
        #         #     j-=1
        #         else:
        #             # i+=1
        #             j-=1

        # return op
        for i in range(len(nums)):
            j,k = i+1,len(nums)-1
            while j<k:
                if (nums[j]+nums[k]<(-nums[i])):
                    j+=1
                    continue
                if (nums[j]+nums[k]>(-nums[i])):
                    k-=1
                    continue
                if (-nums[i]==nums[j]+nums[k]):
                    arr = sorted([nums[i],nums[j],nums[k]])
                    if arr not in op:
                        op.append(arr)
                    k-=1
        return op
                    


        