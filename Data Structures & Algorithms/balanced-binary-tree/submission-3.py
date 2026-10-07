# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diff = 0
        
        def dfs(r):
            if not r:
                return 0

            left = dfs(r.left)
            right = dfs(r.right)

            self.diff = max(self.diff, abs(right - left))
            return 1 + max(right, left)
        
        dfs(root)
        
        if self.diff > 1:
            return False

        return True


