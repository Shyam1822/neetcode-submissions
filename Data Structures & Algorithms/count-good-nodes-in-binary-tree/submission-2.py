# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def curNodeCheck(node,cur_max):
        if not node:
            return []
        
        if node.val>=cur_max:
            return [node.val]+curNodeCheck(node.left,node.val)+curNodeCheck(node.right,node.val)
        
        return curNodeCheck(node.left,cur_max)+curNodeCheck(node.right,cur_max)

class Solution:
        
    def goodNodes(self, root: TreeNode) -> int:

        #30/7/26

        # thinking process:
        '''
        identified it should be a BFS as key element to pass to each eleemnt is the current max in the path
        if the current nodes value is greater than the max identifed in the path, the node is good
        then curr calue is updated and passed on to nodes below it
        '''

        # 31/7/26
        # my understanding for dfs and bfs is mixed up, all these days, have been doing dfs but thought it is bfs

        #thought we should return the elements, but seems like total number is enough

        cur_max = -101

        # return curNodeCheck(root,cur_max)
        return len(curNodeCheck(root,cur_max))

