# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #14/10 random re
        # remembering to use deque and its size

        if not root:
            return []

        q = deque([root])
        op = []

        while q:
            l = len(q)
            cur = []
            for i in range(l):
                cur.append(q[0].val)
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                q.popleft()
                continue
            op.append(cur)
        return op
