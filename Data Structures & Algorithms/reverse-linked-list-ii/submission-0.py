# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left==right:
            return head

        stack=[]
        start=None
        end=None

        node=head
        while node:
            if node.val==left:
                stack.append(node)
                break
            start=node
            node=node.next


        while node:
            if node.val==right:
                stack.append(node)
                end=node.next
                break
            stack.append(node)
            node=node.next

        while stack:
            if not start:
                start=stack.pop()
                head=start
            else:
                start.next=stack.pop()
                start=start.next

        start.next=end

        return head