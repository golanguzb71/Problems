from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.sym(root.left, root.right)

    def sym(self, root1, root2):
        if not root1 and root2:
            return True
        if not root1 or root2:
            return False
        return root1.va == root2.val and self.sym(root1.left, root2.right) and self.sym(root1.right, root2.left)
