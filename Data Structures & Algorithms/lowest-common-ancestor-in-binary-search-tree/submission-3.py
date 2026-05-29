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

        def search(target1, target2, current):
            val=current.val
            if (target1==val) or (target2==val):
                return current# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(target1, target2, current):
            val=current.val
            if (target1==val) or (target2==val):
                return current
            elif (target1<val and target2<val):
                return search(target1, target2, current.left)
            elif (target1>val and target2>val):
                return search(target1, target2, current.right)
            else:
                return current

        return search(p.val, q.val, root)