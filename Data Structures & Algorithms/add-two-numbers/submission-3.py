# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 or not l2:
            return None

        node1=l1
        node2=l2
        newlist=ListNode(None)
        nextnode=newlist

        c=0
        while node1 and node2:
            net=node1.val+node2.val+c
            
            #print(net)
            s=net%10
            c=net//10
            nextnode.next=ListNode(s)
            nextnode=nextnode.next
            node1=node1.next
            node2=node2.next
        
        node=node1 if node1 else node2
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
