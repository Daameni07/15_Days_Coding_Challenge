#111. Minimum Depth of Binary Tree
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # If no left child, go down right subtree
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # If no right child, go down left subtree
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # Both children exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
