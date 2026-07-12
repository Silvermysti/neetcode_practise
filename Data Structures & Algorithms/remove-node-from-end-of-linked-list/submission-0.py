# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if n==1:
            return head.next
        node=head
        length=0
        while node:
            length+=1
            node=node.next
        
        
        n=length-n-1
        i=0
        node=head
        while i<n:
            i+=1
            node=node.next
        
        if node.next:
            node.next=node.next.next

        return head
        