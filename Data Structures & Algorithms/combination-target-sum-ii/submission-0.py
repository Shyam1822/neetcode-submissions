class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #13/9 and 14/9/26
        candidates.sort()
        op = []

        def backtrack(index, path, current_sum):
            
            if current_sum == target:
                op.append(path.copy())
                return
            
            if current_sum > target or index >= len(candidates):
                return

            for i in range(index,len(candidates)):
                if i>index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path,sum(path))
                path.pop()
        
        backtrack(0,[],0)
        return op
            