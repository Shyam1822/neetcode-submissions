class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #13/9/26
        op = []
        def backtrack(index,cur_path):
            # base case to terminate
            if index == len(nums): # meaning we are at the leaf of current path
                op.append(cur_path.copy()) # copying all current possible paths
                return

            cur_path.append(nums[index]) # decision to include current number and traversing with it
            backtrack(index+1,cur_path)

            cur_path.pop() # removing the current element to backtrack and go to alternate path
            backtrack(index+1,cur_path)


        # start with initial index and empty path
        backtrack(0,[])
        return op 

    
