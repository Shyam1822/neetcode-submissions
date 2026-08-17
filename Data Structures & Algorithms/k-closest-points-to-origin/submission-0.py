class Solution:
    def __init__(self):
            self.max_heap = []

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #17/8/26
        # initial though process
        '''
        max heap with k size
        but thought of having the node value like [distance,x,y] and use distance for adding and removing value
        proceeding in that aspect
        '''


        #after some time, got to know we can add tuple to heap element, will take first value to compare

        for x,y in points:
            distance = -(x**2+y**2)**0.5 # negation must for max heap implementation
            heapq.heappush(self.max_heap,(distance,x,y))

            if len(self.max_heap)>k:
                heapq.heappop(self.max_heap)

        return [[x,y] for d,x,y in self.max_heap]
        
        