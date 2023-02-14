from collections import deque


class NodeBinary:
    def __init__(this,val):
        this.left = None #node
        this.right = None #node
        this.val = val #int
   
    def printData(this):
        if this.left:
            #print(this.left.val)
            this.left.printData()
            
        print(this.val)
        
        if this.right:
            #print(this.right.val)
            this.right.printData()        
        
        
            
    def insert(this,val):
        
        if this.val:
            if val < this.val:
                if this.left is None:
                    
                    this.left = NodeBinary(val)
                else:
                    
                    this.left.insert(val)
            if val > this.val:
                if this.right is None:
                    this.right = NodeBinary(val)
                else:
                    this.right.insert(val)                
        else:
            this.val = val
     
    def inOrderTraversal(this,root):
        arr = []
        if root:
            arr = this.inOrderTraversal(root.left)
            arr.append(root.val)
            arr = arr + this.inOrderTraversal(root.right)
        return arr
       
    def preOrderTraversal(this,root):
        arr = []
        if root:
            arr.append(root.val)
            arr = arr + this.preOrderTraversal(root.left)
            arr = arr + this.preOrderTraversal(root.right)
        return arr 
    
    def postOrderTraversal(this,root):
        arr = []
        if root:
            arr = arr + this.preOrderTraversal(root.left)
            arr = arr + this.preOrderTraversal(root.right)
            arr.append(root.val)
        return arr 
    
    def lowestCommonAncestor(self, root, p, q):
        

        if root is None: 
            return None

        if p == root or q == root:

            return root
        left = self.lowestCommonAncestor(root.left, p , q)
        right = self.lowestCommonAncestor(root.right, p , q)
        
        print("left:",left)
        print("right:",right)
        print("====")
        if left is not None and right is not None:

            return root
        if left is None:

            return right
        if right is None:
            return left
    
    def getSuccessor(this,root,n):
        res = None
        if root:
            
            if root.val > n and root.left:
                this.getSuccessor(root.left,n)
            elif root.val < n and root.right:
                this.getSuccessor(root.right,n)
            elif root.val == n:
                res = root
                return res
        print(res)
        return res
    
    def inOrderSuccessor(this, root,n): 
        
        successor = None
        while root:
            if n < root.val:
                successor = root
                root = root.left
            elif n >= root.val:
                root = root.right
            elif root.val == n:
                return root
        return successor
    
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
  
root =  NodeBinary(6)  
root.insert(2)
root.insert(8)
root.insert(0)
root.insert(4)
root.insert(7)
root.insert(9)

def lowestCommonAncestor(root, p, q):
    
    if root is None: 
        return None

    if p == root.val or q == root.val:

        return root
    left = lowestCommonAncestor(root.left, p , q)
    right = lowestCommonAncestor(root.right, p , q)
    
    if left is not None and right is not None:

        return root
    if left is None:

        return right
    if right is None:
        return left

a = lowestCommonAncestor(root,0,9)
print(a.val)
