"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #2/10/26

        if not node:
            return None 

        map_dict = {}

        root = Node()

        cur = Node(node.val)
        root.neighbors = [cur]
        map_dict[node] = cur

        def dfs(node,copy_node):

            for i in node.neighbors:
                if i in map_dict:
                    # need to attach already existing nodes as well
                    copy_node.neighbors.append(map_dict[i])
                    continue
                new_node = Node(i.val)
                map_dict[i] = new_node
                copy_node.neighbors.append(new_node)
                dfs(i,new_node)
        
        dfs(node,cur)
        return root.neighbors[0]

        

        


        

        