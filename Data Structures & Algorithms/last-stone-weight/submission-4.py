class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use direct heapq to solve thsi time
        st = [-i for i in stones]
        heapq.heapify(st)
        
        while len(st)>1:
            a,b = heapq.heappop(st),heapq.heappop(st)
            if a!=b:
                heapq.heappush(st,-(abs(a-b)))
        return 0 if (not st) else -st[0]