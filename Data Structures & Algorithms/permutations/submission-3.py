class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 26/9/26 r1

        op = []
        s = len(nums)
        bool_arr = [False]*s

        def backtrack(bool_arr,path):
            if len(path) == s:
                op.append(path.copy())
                return
            
            for i in range(s):
                if bool_arr[i]:
                    continue
                
                path.append(nums[i])
                bool_arr[i] = True
                backtrack(bool_arr,path)
                path.pop()
                bool_arr[i] = False

                
            
        
        backtrack(bool_arr,[])
        return op