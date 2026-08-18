class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # have to try again
        # fun fact this could be solved with simple list sort, feeling becoming to obsessed and blind folded by theme, have to develop the sense of identifying other themes as well
        

        #18/8/26 trying again today after yesterday

        max_heap = []

        for x,y in points:
            dis = x**2+y**2

            max_heap.append([-dis,x,y])

        heapq.heapify(max_heap)

        while len(max_heap)>k:
            heapq.heappop(max_heap)

        return [[x,y] for dis,x,y in max_heap]