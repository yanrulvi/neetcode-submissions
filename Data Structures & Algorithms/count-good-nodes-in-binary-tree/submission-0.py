# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        res = 0
        stack = [(root, root.val)]

        while stack:
            node, max_ = stack.pop()

            if node.val >= max_:
                res += 1
                max_ = node.val


            if node.left is not None:
                stack.append((node.left, max_))
            if node.right is not None:
                stack.append((node.right, max_))

        return res