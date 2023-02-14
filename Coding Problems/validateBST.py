class Solution:
    def isValidBST(self, root,lessThan = float('inf'), largerThan = float('-inf')) -> bool:
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        else:
            return self.isValidBST(root.left,min(root.val,lessThan),largerThan) and \
                   self.isValidBST(root.right,lessThan,max(root.val,largerThan))