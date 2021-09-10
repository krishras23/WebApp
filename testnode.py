import node

node1 = node.Node("John")
print(node1.get_name())
print(node1.get_next())

node2 = node.Node("Krish")
node1.set_next(node2)

print(node1.get_next().get_name())

node3 = node.Node("Anything")
node2.set_next(node3)

print("while loop")

new_node_list = []

n = node1
while n is not None:
    print(n.get_name())
    if n.get_name() == "Krish":
        new_node_list.append(n)
    n = n.next

print ("print filter")
for x in new_node_list:
    print(x.get_name())
