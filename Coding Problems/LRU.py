
from platform import node


class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class singlyLinkedList:
    def __init__(self,capacity) -> None:
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = 5
        self.dic = {}
        
    def _add(self,Node):
        p = self.tail.prev
        p.next = Node
        Node.next = self.tail
        Node.prev = p
        self.tail.prev = Node
    
    def _remove(self,Node):
        p = Node.prev
        n = Node.next
        
        p.Next = n
        n.prev = p  
              
    def addNode(self,key,val):
        if key in self.dic:
            self._remove(self.dic[key])
        newNode = Node(key,val)
        self._add(newNode)
        self.dic[key] = newNode
        if len(self.dic) > self.capacity:
            self._remove(self.dic[key])
        
"""
Steps:-
create node with key value prev and next
create ssl with head tail capacity and dic and assign thosem to each other

add:-
    check if the key is in dic, if yes then remove
    to add the node, add before tail

add to dictionary and check if greater than capacity then delete.



"""