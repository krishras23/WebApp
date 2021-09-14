class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def set_left(self, l):
        self.left = l

    def get_left(self):
        return self.left

    def set_right(self, r):
        self.right = r

    def get_right(self):
        return self.right

