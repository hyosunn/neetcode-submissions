# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        copy = root
        if not copy:
            return root
        else:
            temp = copy.left
            copy.left = copy.right
            copy.right = temp

            copy.left = self.invertTree(copy.left)
            copy.right = self.invertTree(copy.right)
            return copy
        
        
        
        