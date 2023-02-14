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
    
    
root = NodeBinary(4)
root.insert(23)
root.insert(20)
root.insert(13)
root.insert(10)
root.insert(33)
root.insert(2)
root.insert(1)
root.insert(3)

#             4
#         2       23                
#    1      3   20   33
#             13
#           10

from collections import deque
def levelOrder(root,num):
    
    res = []
    q = deque()
    if root:
        q.append(root)
    directionLeftToRight = True    
    returnFlag = False
    while q:
        val = []
        childNodes = deque()
        for i in range(len(q)):
            if directionLeftToRight == True:
                node = q.popleft()
                if returnFlag == True:
                    print("ans",node.data)
                    return node.data
                val.append(node.data)
                if node.left:
                    childNodes.append(node.left)
                if node.right:
                    childNodes.append(node.right)
                if node.data == num:
                    returnFlag = True
                

            else:
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    childNodes.append(node.left)
                if node.right:
                    childNodes.append(node.right)   
        returnFlag = False
        
        q = childNodes
        #directionLeftToRight = False if directionLeftToRight else True
        #print(val)
        res.append(val)
    if returnFlag == False:
        print("ans",None)
        return None
    
    return res
levelOrder(root,3)
