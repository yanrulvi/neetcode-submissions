# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "$#"
        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))


    def isSubString(self, t: str, s: str) -> bool:
        d = Counter(t)
        k = len(t)
        l = 0
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) - 1
            if d[s[r]] == 0:
                del d[s[r]]

            if r >= k:
                d[s[l]] = d.get(s[l], 0) + 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1

            
            if not d and t == s[l: r + 1]:
                return True
        return True if not d else False
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False

        ser_root = self.serialize(root)
        ser_subroot = self.serialize(subRoot)

        return self.isSubString(ser_subroot, ser_root)
        
