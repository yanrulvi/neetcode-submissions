# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseSubList(self, head: Optional[ListNode], next_head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = next_head, head
        while cur != next_head:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        i = 0
        cur = head
        group_head = head
        res = ListNode()
        cur_res = res

        while cur:
            i += 1
            cur = cur.next

            if i % k == 0:
                next_group = cur
                cur_res.next = self.reverseSubList(group_head, next_group)
                cur_res = group_head
                group_head = next_group

        if res.next is None:
            return head

        return res.next