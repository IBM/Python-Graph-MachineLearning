class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

"""
Steps:-
if root is none return 0
else  1 +max(recursion left tree, recursion right tree)


"""