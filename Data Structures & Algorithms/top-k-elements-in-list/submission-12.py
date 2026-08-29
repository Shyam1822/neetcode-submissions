class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #28/5/26
        if len(nums)==1:
            return nums
        # frq_lst = [[]] * (len(nums)+1) # this create shallow copy(list is mutable, same ref obj)
        frq_lst = [[] for _ in range(len(nums) + 1)]


        hasmp = {}

        for i in nums:
            hasmp[i] = hasmp.get(i,0)+1
        # print(hasmp)

        for i in hasmp:
            # print(i,hasmp[i])
            frq_lst[hasmp[i]].append(i)
            # print(frq_lst)

        # print(frq_lst)

        op = []
        count = 0


        for i in range(len(frq_lst) - 1, 0, -1):
            if (frq_lst[i]):
                op.extend(frq_lst[i])
                count += len(frq_lst[i]) 
            if(count>=k):
                return op
        
        return op