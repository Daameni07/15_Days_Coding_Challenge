#104. Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: empty tree has depth 0
        if not root:
            return 0
        # Recursively find depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # Depth of current node = 1 (itself) + max depth of children
        return 1 + max(left_depth, right_depth)
