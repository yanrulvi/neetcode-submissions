# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
            
        q = deque([root])
        res = []
        i = 1
        j = 0
        while q:
            node = q.popleft()

            if node.left is not None:
                q.append(node.left)
                j += 1
            if node.right is not None:
                q.append(node.right)
                j += 1
            
            i -= 1

            if i == 0:
                res.append(node.val)
                i = j
                j = 0
        return res
