class MedianFinder:
    # 12/9/26
    def __init__(self):
        # self.min_heap = []
        # self.max_heap = []
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        l = len(self.arr)
        if l%2:
            return self.arr[l//2]
        return (self.arr[(l//2)-1]+self.arr[l//2])/2
        