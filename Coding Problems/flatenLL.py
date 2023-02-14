
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.child = None

n1 = Node(1)
n2= Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)
n11 = Node(11)
n12 = Node(12)


n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n7.next = n8
n8.next = n9
n9.next = n10
n11.next = n12


n3.child = n7
n8.child = n11





root = n1

class Solution:
    def flatten(self, head):
        cur = head
        tail = None
        while cur:
            print(cur.val)
            if cur.child:
                tail = cur.next
                cur.next,tail = self.flatten(cur.child)
                #cur.next.prev = cur
                cur.child = None
            
                    
                #
            
            cur = cur.next
        
        if tail:
            cur.next = tail
            return head,tail
        else:
            return head,None

s = Solution()
ans = s.flatten(root)

"""
while ans:
    print(ans.val)
    ans = ans.next
"""