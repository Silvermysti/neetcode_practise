"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return

        visited=set()
        newhead=Node(head.val)
        dictionary=defaultdict()

        def copylist(node):
            if not node or node.val in visited:
                return
            newnode=Node(node.val)
            dictionary[node.val]=[node.next.val if node.next else None, node.random.val if node.random else None,newnode]
            visited.add(node.val)
            copylist(node.next)
            copylist(node.random)
        copylist(head)
        #print (dictionary[3][2])

        for i in dictionary.keys():
            nextval,randomval = dictionary[i][0], dictionary[i][1]
            dictionary[i][2].next=dictionary[nextval][2] if nextval else None
            dictionary[i][2].random=dictionary[randomval][2] if randomval else None

        return dictionary[head.val][2]