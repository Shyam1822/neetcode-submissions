# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # from the next problem, got the idea that we can use string serialization here too

        def serialize(p):
            if not p:
                return "n"
            
            left = serialize(p.left)
            right = serialize(p.right)

            op = "'"+left+str(p.val)+right+"'"
            print(op)
            return op
        return serialize(p)==serialize(q)
