from linkedlist import LinkedList
from node import Node

node1 = Node("first")
ln = LinkedList()
ln.append_node(node1)
# ln.print_nodes()
node2 = Node("second")
ln.append_node(node2)
ln.print_nodes()

print(ln.find_node(node2))
print(ln.find_node(Node("foo")))
