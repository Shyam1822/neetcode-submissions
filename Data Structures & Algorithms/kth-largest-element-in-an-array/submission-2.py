class Solution:
    def __init__(self):
        self.max_heap = []
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 18/8/26
        # with sorting
        # return sorted(nums)[::-1][k-1]

        '''# without sorting, using heap'''
        '''Gpt gave an easy and valid solution, instead of this sibling uncle logic, just pop k times, u will get the kth element :)'''

        # #gonna check only for right nodes, if greater than left, swap with left node
        # def sibling_check(self,i):
        #     # since negative value present, inverse comparision
        #     if self.max_heap[i]<self.max_heap[i-1]:
        #         self.max_heap[i],self.max_heap[i-1] = self.max_heap[i-1],self.max_heap[i]
            
        # # key part, if sibling of parent is lesser than current left node, need to swap that as well
        # def uncle_check(self,i):
        #     while i>2:
        #         parent = i-


        nums = [-x for x in nums]
        for i in nums:
            heapq.heappush(self.max_heap,i)
        for i in range(k-1): # k-1, beacuse during kth time, kth element will be removed, either store it and return or stop before it and return top heap value
            heapq.heappop(self.max_heap)
        return -(self.max_heap[0])

        

        