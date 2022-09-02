def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root is None:
        return
    if root == p or root == q:
        return root
    
    left = self.lowestCommonAncestor(root.left,p,q)
    right = self.lowestCommonAncestor(root.right,p,q)
    
    if left and right:
        return root
    if right is None:
        return left
    if left is None:
        return right

"""
Steps:-
if p or q is none return None
if root found in p or q then return root
recursively iterate left sub tree
recursively iterate right sub tree
if values found in left subtree and right subtree then return root
else return left or right



"""