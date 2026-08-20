# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def check_tree(node,min_v,max_v):
    if not node:
        return True

    if node.val>min_v and node.val<max_v:
        return check_tree(node.left,min_v,node.val) and check_tree(node.right,node.val,max_v)
    
    return False
    

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return check_tree(root,float('-inf'),float('inf'))