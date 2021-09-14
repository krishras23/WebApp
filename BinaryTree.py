from TreeNode import TreeNode


class BinaryTree:
    def __init__(self, rootval):
        self.root = TreeNode(rootval)

    def append_left(self, TreeNode1):
        x = self.root
        while x.left is not None:
            x = x.left
        x.left = TreeNode1

    def append_right(self, TreeNode1):
        x = self.root
        while x.right is not None:
            x = x.right
        x.right = TreeNode1