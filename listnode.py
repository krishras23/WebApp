from node import Node


class ListNode:
    def __init__(self):
        self.head = Node("head")

    def print_nodes(self):
        n = self.head.next
        while n is not None:
            print(n.get_name())
            n = n.next

    def append_node(self, node):
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = node

    def find_node(self, node):
        n = self.head
        while n is not None:
            if n.get_name() == node.get_name():
                return True
            n = n.next
        return False

