# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeaf(root1) == self.getLeaf(root2)
    
    def getLeaf(self, root: Optional[TreeNode]) -> list:
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        
        return self.getLeaf(root.left) + self.getLeaf(root.right)