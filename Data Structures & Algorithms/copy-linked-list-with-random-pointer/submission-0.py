"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        copyD = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            copyD[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = copyD[cur]
            copy.next = copyD[cur.next]
            copy.random = copyD[cur.random]
            cur = cur.next
        
        return copyD[head]