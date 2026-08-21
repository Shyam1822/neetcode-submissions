class Solution:
    # def freq_map(self,tasks):
    #     freq_map = []
    #     for i in set(tasks):
    #         freq_map.append(-tasks.count(i)) # for max_heap, also only frequency is enough it seems
    #     return freq_map
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #21/8/26
        
        # saw the hints, saying to use freq map for each task, and push max freq elements into heap and pop them into cooling data structure

        # max_heap = self.freq_map(tasks)

        count = Counter(tasks)
        max_heap = [-c for c in count.values()]
        heapq.heapify(max_heap)
        wait_list = deque()

        time = 0

        while max_heap or wait_list:
            time+=1

            if max_heap:
                cnt = 1+heapq.heappop(max_heap) # reduing freq of that task
                if cnt:
                    wait_list.append([cnt,time+n])
                
            if wait_list and wait_list[0][1] == time:
                heapq.heappush(max_heap, wait_list.popleft()[0])
        
        return time
                





