def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = curr = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = ListNode(list1.val)
            list1 = list1.next
        else:
            curr.next = ListNode(list2.val)
            list2 = list2.next
        curr = curr.next

    if list1:
        curr.next = list1
    if list2:
        curr.next = list2
    return dummy.next

"""
Steps:-

while both list are present
add value from linked list which is smaller
do current.next

if l1 remaining then add l1 or l2

"""