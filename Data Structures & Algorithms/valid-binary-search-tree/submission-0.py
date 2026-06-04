# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node):
            l=True
            r=True
            if node.left:
                if node.val<node.left.val:
                    return False
                l=traverse(node.left)
            if node.right:
                if node.val>node.right.val:
                    return False
                r=traverse(node.right)
            
            if l==False or r==False:
                return False
            else:
                return True
        
        return traverse(root)

            