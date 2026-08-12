# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_ = 0
        cursor = head
        while cursor:
            len_ += 1
            cursor = cursor.next

        if n == len_:
            return head.next

        i = 0
        prev = None
        cursor = head
        while i < len_ - n:
            prev = cursor
            cursor = cursor.next
            i += 1
        prev.next = cursor.next

        return head