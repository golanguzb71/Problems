class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_leaf(root):
    return root and not root.left and not root.right


def count_leaves(root: TreeNode) -> int:
    if not root:
        return 0
    if is_leaf(root):
        return 1
    return count_leaves(root.left)+ count_leaves(root.right)
