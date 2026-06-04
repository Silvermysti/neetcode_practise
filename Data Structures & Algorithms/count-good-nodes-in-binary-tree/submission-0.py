# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.path=[-101]
        self.res=0

        def traverse(node):
            print(node.val)
            print(self.path)
            if node.val>=max(self.path):
                self.res+=1
                print("res:", self.res)
            self.path.append(node.val)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            self.path.pop()
            print(" ")
        
        traverse(root)
        return self.res
        

