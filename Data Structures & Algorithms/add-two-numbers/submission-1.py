# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add_one = 0
        res = ListNode(0)
        cur = res
        while l1 or l2:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            cur.next = ListNode((val1 + val2 + add_one) % 10)
            add_one = 1 if val1 + val2 + add_one > 9 else 0
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            cur = cur.next
        if add_one == 1:
            cur.next = ListNode(1)
        return res.next