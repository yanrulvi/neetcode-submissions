# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(val=-1000)
        c1 = list1
        c2 = list2
        c_res = res
        while c1 and c2:
            if c1.val <= c2.val:
                c_res.next = ListNode(val=c1.val)
                c1 = c1.next
            else:
                c_res.next = ListNode(val=c2.val)
                c2 = c2.next

            c_res = c_res.next
        
        c_res.next = c1 if c1 else c2
        return res.next