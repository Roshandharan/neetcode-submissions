"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
       if not node:
        return None
       
       stk = []
       start = node
       stk.append(start)
       visit = set()
       visit.add(start)
       o_to_n = {}

       while stk:
        node = stk.pop()
        o_to_n[node] = Node(val=node.val)
        for nei in node.neighbors:
            if nei not in visit:
                stk.append(nei)
                visit.add(nei)
       
       for old_node,new_node in o_to_n.items():
        for nei in old_node.neighbors:
            new_nei = o_to_n[nei]
            new_node.neighbors.append(new_nei)
        
       return o_to_n[start] 
    #tc: O(v+E)
    #sc: O(v)
    # create new node in reference to the old nodes and dfs that and map neighbors


