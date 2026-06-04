# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node,mini,maxi):
            val=node.val
            print(val,mini,maxi)

            if val<=mini or val>=maxi:
                print("False")
                return False

            if node.left:
                l=traverse(node.left,mini,node.val)
            else:
                l=True

            if node.right:
                r=traverse(node.right,node.val,maxi)
            else:
                r=True

            if l==False or r==False:
                return False
            else:
                return True
            



        res=traverse(root,-math.inf,math.inf)
        return res

            