class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

"""
Steps:-
if both empty, return True
if p or q empty or their values dont match then return False
do recursion by pasing left of both trees and right of both trees

"""