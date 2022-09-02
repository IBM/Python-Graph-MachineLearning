def addTwoNumbers(self, l1, l2) :
    head = tail = ListNode()
    carry = 0
    while l1 or l2 or carry:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        
        val = l1_val + l2_val + carry
        carry = val // 10
        val = val % 10
        
        tail.next = ListNode(val)
        tail = tail.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return head.next

"""
Steps:-
while loop till both list or carry are present
get values of linked list and add with carry
get carry wth division
get remainder with mod
add mod to remainder and pass carry

"""