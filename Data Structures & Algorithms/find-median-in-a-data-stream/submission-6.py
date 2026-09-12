class MedianFinder:
    # 12/9/26
    # non-efficient soln with array sorting
    # def __init__(self):
    #     # self.min_heap = []
    #     # self.max_heap = []
    #     self.arr = []

    # def addNum(self, num: int) -> None:
    #     self.arr.append(num)
    #     self.arr.sort()
        

    # def findMedian(self) -> float:
        
    #     l = len(self.arr)
    #     if l%2:
    #         return self.arr[l//2]
    #     return (self.arr[(l//2)-1]+self.arr[l//2])/2

    def __init__(self):
        self.min_heap = []  # min of larger half
        self.max_heap = []  # max of small half
        self.size = 0

    def addNum(self,num):
        heapq.heappush(self.max_heap,-num)
        if self.min_heap and self.min_heap[0]<(-self.max_heap[0]):
            swap_a = -heapq.heappop(self.min_heap)
            swap_b = -heapq.heappop(self.max_heap)
            heapq.heappush(self.max_heap,swap_a)
            heapq.heappush(self.min_heap,swap_b)
        
        if (len(self.min_heap) > len(self.max_heap)) or len(self.min_heap)+1<len(self.max_heap):
            ele = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-ele)
        self.size+=1

    def findMedian(self):
        if self.size%2:
            return -self.max_heap[0]
        return (self.min_heap[0]-self.max_heap[0])/2






        