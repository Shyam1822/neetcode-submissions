class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # this seems the most intuitive for me

        if n==0:
            return len(tasks)
        counter = Counter(tasks)
        item = counter.most_common(1)
        task, max_freq = item[0][0], item[0][1]
        c = 0
        for key, value in counter.items():
            if max_freq==value:
                c+=1

        return max(((max_freq-1)*(n+1) + c), len(tasks))