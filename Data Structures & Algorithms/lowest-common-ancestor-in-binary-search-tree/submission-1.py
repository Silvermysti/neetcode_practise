# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        qnodes={}
        pnodes={}

        def searchq(target,qnodes,current):
            qnodes[current.val]=current
            if current.val==target:
                return qnodes
            elif(current.val>target):
                return searchq(target,qnodes,current.left)
            else:
                return searchq(target,qnodes,current.right)
        
        qnodes=searchq(q.val, qnodes, root)
        print(qnodes)
        
        def searchp(target, current, prev):
            if (current.val not in qnodes):
                return prev           
            pnodes[current.val]=current
            if current.val==target:
                return current
            elif(current.val>target):
                return searchp(target,current.left, current)
            else:
                return searchp(target,current.right, current)
        
        return searchp(p.val, root, root)