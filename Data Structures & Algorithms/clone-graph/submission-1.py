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
        
        visited={}

        def clone(node):
            if node.val in visited:
                return visited[node.val]

            newnode=Node(node.val,[])
            visited[node.val]=newnode

            for neighbor in node.neighbors:
                newnode.neighbors.append(clone(neighbor))
            
            return newnode

        return clone(node)
