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
        
        visited=set()
        res=Node(node.val,[])
        copynode=res


        def clone(copynode, node):

            visited.add(node.val)
            for neighbour in node.neighbors:
                copyneighbour=Node(neighbour.val,[copynode])
                if neighbour.val not in visited:
                    copynode.neighbors.append(copyneighbour)
                    clone(copyneighbour,neighbour)

            #print(copynode.val, [i.val for i in copynode.neighbors])

        clone(copynode, node)
        return res
