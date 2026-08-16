# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        op = []

        queue = deque([root])
        while queue:
            cur_len = len(queue)
            for i in range(cur_len-1):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                
                
                if node.right:
                    queue.append(node.right)

            cur_vis_node = queue.popleft()
            op.append(cur_vis_node.val)
             
            if cur_vis_node.left:
                queue.append(cur_vis_node.left)
            
            if cur_vis_node.right:
                queue.append(cur_vis_node.right) 
        return op