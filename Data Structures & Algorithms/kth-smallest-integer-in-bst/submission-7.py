# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.curr_k_val = 0
        self.k = -1
        self.op = -1
    
    def small_search(self, node):
        if node.left:
            result = self.small_search(node.left)
            if result is not None:
                return result

        self.curr_k_val += 1

        if self.curr_k_val == self.k:
            return node.val

        if node.right:
            result = self.small_search(node.right)
            if result is not None:
                return result

        return None 

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # same day 24/8/26
        # same logic written by me in before code, gpt gave optimization to stop the loop if op value set, no need of op.k at all

        self.k = k

        return self.small_search(root)
        
