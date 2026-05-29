# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return[]

        levels={}

        def traverse(current,level):

            if level not in levels:
                levels[level]=[current.val]
            else:
                levels[level].append(current.val)

            if current.left:
                traverse(current.left, level+1)
            if current.right:
                traverse(current.right, level+1)

            
        traverse(root, 0)

        return list(levels.values())

        