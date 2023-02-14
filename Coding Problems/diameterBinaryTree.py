class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.diameter
        