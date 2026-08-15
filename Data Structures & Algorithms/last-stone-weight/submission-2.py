class Solution:

    def __init__(self):
        self.max_heap = []

    def add(self,val):
        self.max_heap.append(val)
        self.upward_check(len(self.max_heap)-1)

    def upward_check(self,i):
        if i == 0:
            return

        #find parent

        par_idx = (i-1)//2
        if self.max_heap[par_idx]>=self.max_heap[i]:
            return
        # if new element is bigger than parent, swap
        self.max_heap[par_idx],self.max_heap[i] = self.max_heap[i],self.max_heap[par_idx]

        self.upward_check(par_idx)

    def downward_check(self,idx):
        # find childs
        left,right = idx*2+1,idx*2+2

        if len(self.max_heap)<=left:
            return

        larger = left

        if len(self.max_heap)>right and self.max_heap[right]>self.max_heap[left]:
            larger = right
        
        if self.max_heap[larger]<=self.max_heap[idx]:
            return

        #swap
        self.max_heap[larger],self.max_heap[idx] = self.max_heap[idx],self.max_heap[larger]

        self.downward_check(larger)
            
        

    def destroy_stones(self):
        while len(self.max_heap)>=2:

        # remove 1st element(1st largest), then replace last eleemnt with root, then heapify down, then remove 2nd largest element again

            largest = self.max_heap[0]
            self.max_heap[0] = self.max_heap[-1]
            self.max_heap.pop()

            self.downward_check(0)

            large_2nd = self.max_heap[0]
            self.max_heap[0] = self.max_heap[-1]
            self.max_heap.pop()

            self.downward_check(0)

            if largest!=large_2nd:
                self.add(largest-large_2nd)
        
        if len(self.max_heap)==1:
            return self.max_heap[0]
        return 0
            

    def lastStoneWeight(self, stones: List[int]) -> int:
        #15/8/26
        # requirement:
        '''
        consider all elements in the array, find top 2 stones at each stage, and destroy both or save tehir abs value
        '''

        #approach:
        #create a max heap(o(n)), then alter elements until one or no element exist

        for i in stones:
            self.add(i)
        
        return self.destroy_stones()




        
