class Solution:
    def flatten(self, head):
        cur = head
        while cur:
            if cur.child:
                tail = cur.next
                cur.next = self.flatten(cur.child)
                cur.next.prev = cur
                cur.child = None
                
                while cur.next:
                    cur = cur.next
                    
                cur.next = tail
                if tail:
                    tail.prev = cur
            
            cur = cur.next
        
        return head