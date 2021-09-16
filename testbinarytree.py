from BinaryTree import BinaryTree
from TreeNode import TreeNode

z = BinaryTree("str")
x = BinaryTree(89)

x.append_left(TreeNode(855))
x.append_right(TreeNode(82255))

# Test Tree Node

root = TreeNode("val")

root.left = TreeNode("1st left")
root.right = TreeNode("1st right")
root.left.left = TreeNode("more left")

tn2 = TreeNode("temp")

root.get_right().set_right(tn2)
