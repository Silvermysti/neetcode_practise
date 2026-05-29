# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rightmost={}

        def traverse(current, level):
            rightmost[level]=current.val
            if current.left:
                traverse(current.left, level+1)
            if current.right:
                traverse(current.right, level+1)
            print(rightmost)
        
        traverse(root, 0)
        
        return list(rightmost.values())
            


        