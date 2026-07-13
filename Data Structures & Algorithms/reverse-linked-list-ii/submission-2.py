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

        index=1
        node=head
        while node:
            if index==left:
                stack.append(node)
                break
            start=node
            node=node.next
            index+=1


        while node:
            if index==right:
                stack.append(node)
                end=node.next
                break
            stack.append(node)
            node=node.next
            index+=1
        #else

        while stack:
            if not start:
                start=stack.pop()
                head=start
            else:
                start.next=stack.pop()
                start=start.next

        start.next=end

        return head