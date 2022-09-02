class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

"""
Steps:--
while value in linked list
In temp set next value
set next value as previous
set previous value as current
set current as temp

"""