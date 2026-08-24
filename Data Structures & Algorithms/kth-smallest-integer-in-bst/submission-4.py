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
    
    def small_search(self,node):
        
        if node.left:
            self.small_search(node.left)
        
        self.curr_k_val+=1
        if self.curr_k_val==self.k:
            self.op = node.val
            return

        if node.right:
            self.small_search(node.right)
        
        return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #24/8/26
        self.k = k

        self.small_search(root)
        return self.op