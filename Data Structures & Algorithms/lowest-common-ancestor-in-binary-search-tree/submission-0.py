# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        way1 = [root]
        way2 = [root]

        node1 = root
        node2 = root

        while node1.val != p.val:
            if p.val < node1.val:
                node1 = node1.left
            else:
                node1 = node1.right
            way1.append(node1)
        
        while node2.val != q.val:
            if q.val < node2.val:
                node2 = node2.left
            else:
                node2 = node2.right
            way2.append(node2)

        res_node = TreeNode()
        for i in range(min(len(way1), len(way2))):
            if way1[i].val == way2[i].val:
                res_node = way1[i]
                continue
            else:
                break
        return res_node