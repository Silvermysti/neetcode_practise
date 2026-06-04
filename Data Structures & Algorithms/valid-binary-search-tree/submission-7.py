# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def traverse(node,mini,maxi):
            if not node:
                return True

            if not (mini<node.val<maxi):
                return False

            return (traverse(node.left,mini,node.val) and traverse(node.right,node.val,maxi))

        return traverse(root,-math.inf,math.inf)

            