# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 or not l2:
            return None

        newlist=ListNode(None)
        nextnode=newlist

        c=0
        while l1 and l2:
            net=l1.val+l2.val+c
            
            #print(net)
            s=net%10
            c=net//10
            nextnode.next=ListNode(s)
            nextnode=nextnode.next
            l1=l1.next
            l2=l2.next
        
        node=l1 if l1 else l2
        while node:
            net=node.val+c
            #print(net)
            s=net%10
            c=net//10
            nextnode.next=ListNode(s)
            nextnode=nextnode.next
            node=node.next
        
        if c>0:
            nextnode.next=ListNode(c)

        return newlist.next
