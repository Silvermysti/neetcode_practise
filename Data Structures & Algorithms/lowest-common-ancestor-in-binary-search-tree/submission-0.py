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
        
        def searchp(target, pnodes, current):
            if (current.val not in qnodes):
                return pnodes
            
            pnodes[current.val]=current
            if current.val==target:
                return pnodes
            elif(current.val>target):
                return searchp(target,pnodes,current.left)
            else:
                return searchp(target,pnodes,current.right)

        pnodes=searchp(p.val, pnodes, root)



        return pnodes[min(pnodes.keys())]