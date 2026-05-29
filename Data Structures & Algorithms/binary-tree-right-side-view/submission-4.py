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

        res=[]

        def traverse(current, level):
            if level>len(res):
                res.append(current.val)
            if current.right:
                traverse(current.right, level+1)
            if current.left:
                traverse(current.left, level+1)
            print(res)
        
        traverse(root, 1)
        
        return res
            


        