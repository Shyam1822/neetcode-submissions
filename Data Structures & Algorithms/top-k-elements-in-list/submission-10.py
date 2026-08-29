class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        max_heap = []
        for i in nums:
            freq[i] = freq.get(i,0)+1
        
        max_heap = [[-count,val] for val,count in freq.items()]
        # max_heap.append([-nums.count(i),i])
        heapq.heapify(max_heap)

        op = []

        for i in range(k):
            op.append(heapq.heappop(max_heap)[1])
        
        return op