class Node:
    def __init__(this,val):
        this.val = val
        this.next = None
        this.child = None
        this.prev = None

class singlyLinkedList:
    def __init__(this):
        this.head = None
        
    def addNode(this,val):
        if this.head is None:
            this.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = this.head
            this.head = new_node
            
    def printNode(this,head):
        node = this.head
        if node:
            print(node.val)
            node = node.next
            this.printNode(node)
            
s = singlyLinkedList()
s.addNode(1)
print(s)