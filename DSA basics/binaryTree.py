class NodeBinary:
    def __init__(this,data):
        this.left = None #node
        this.right = None #node
        this.data = data #int
   
    def printData(this):
        if this.left:
            #print(this.left.data)
            this.left.printData()
            
        print(this.data)
        
        if this.right:
            #print(this.right.data)
            this.right.printData()        
        
        
            
    def insert(this,data):
        
        if this.data:
            if data < this.data:
                if this.left is None:
                    
                    this.left = NodeBinary(data)
                else:
                    
                    this.left.insert(data)
            if data > this.data:
                if this.right is None:
                    this.right = NodeBinary(data)
                else:
                    this.right.insert(data)                
        else:
            this.data = data
     
    def inOrderTraversal(this,root):
        arr = []
        if root:
            arr = this.inOrderTraversal(root.left)
            arr.append(root.data)
            arr = arr + this.inOrderTraversal(root.right)
        return arr
       
    def preOrderTraversal(this,root):
        arr = []
        if root:
            arr.append(root.data)
            arr = arr + this.preOrderTraversal(root.left)
            arr = arr + this.preOrderTraversal(root.right)
        return arr 
    
    def postOrderTraversal(this,root):
        arr = []
        if root:
            arr = arr + this.preOrderTraversal(root.left)
            arr = arr + this.preOrderTraversal(root.right)
            arr.append(root.data)
        return arr 
    
    def lowestCommonAncestor(self, root, p, q):
        

        if root is None: 
            return None

        if p == root or q == root:

            return root
        left = self.lowestCommonAncestor(root.left, p , q)
        right = self.lowestCommonAncestor(root.right, p , q)
        
        if left is not None and right is not None:

            return root
        if left is None:

            return right
        if right is None:
            return left
    
    def getSuccessor(this,root,n):
        res = None
        if root:
            
            if root.data > n and root.left:
                this.getSuccessor(root.left,n)
            elif root.data < n and root.right:
                this.getSuccessor(root.right,n)
            elif root.data == n:
                res = root
                return res
        print(res)
        return res
    
    def inOrderSuccessor(this, root,n): 
        
        successor = None
        while root:
            if n < root.data:
                successor = root
                root = root.left
            elif n >= root.data:
                root = root.right
            elif root.data == n:
                return root
        return successor
    
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))