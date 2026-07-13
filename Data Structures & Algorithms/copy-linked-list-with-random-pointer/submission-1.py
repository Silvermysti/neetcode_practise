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
        dictionary=dict()

        node=head
        while node:
            dictionary[node]=Node(node.val)
            node=node.next

        for node in dictionary.keys():
            dictionary[node].next=dictionary[node.next] if node.next else None
            dictionary[node].random=dictionary[node.random] if node.random else None
        
        return dictionary[head]