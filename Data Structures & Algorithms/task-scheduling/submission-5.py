class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #22/8/26
        # trying both normal way and math way

        #math way
        if n==0:
            return len(tasks)
        
        freq = []
        for i in set(tasks):
            freq.append(tasks.count(i))
        
        max_count = freq.count(max(freq))

        return max((max(freq)-1)*(n+1)+max_count,len(tasks))