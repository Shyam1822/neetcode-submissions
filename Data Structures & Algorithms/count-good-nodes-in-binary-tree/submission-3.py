# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.op = 0
    
    def good_node_check(self,node,cur_max):
        if not node:
            return
        
        if cur_max>node.val:
            self.good_node_check(node.left,cur_max)
            self.good_node_check(node.right,cur_max)
            return
        
        self.op+=1
        self.good_node_check(node.left,node.val)
        self.good_node_check(node.right,node.val)


    def goodNodes(self, root: TreeNode) -> int:
        #20/8/26

        cur_max = -101

        self.good_node_check(root,cur_max)

        return self.op

        