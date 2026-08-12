# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([(root, 1)])
        res = defaultdict(list)

        while queue:
            node, cur_level = queue.popleft()
            res[cur_level].append(node.val)
            if node.left is not None:
                queue.append((node.left, cur_level + 1))
            if node.right is not None:
                queue.append((node.right, cur_level + 1))

        return list(res.values())   