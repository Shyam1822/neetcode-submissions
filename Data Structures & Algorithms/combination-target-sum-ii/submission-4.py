class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 24/9/26 r1

        candidates.sort()

        op = []
        size = len(candidates)

        def backtrack(index,path,cur_sum):
            if cur_sum==target:
                op.append(path.copy())
                return
            
            # if cur_sum>target or index==size:
            #     return

            # this removal of logic and checking it before iteration reduces lot of time take
            
            for i in range(index,size):
                ele = candidates[i]
                if i>index and ele == candidates[i-1]:
                    continue

                if cur_sum + ele > target: # this condition before going into recursive call
                    break
                path.append(ele)
                backtrack(i+1,path,cur_sum+ele)
                path.pop()

        backtrack(0,[],0)
        return op
