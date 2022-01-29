import node

node1 = node.Node("Jack")
node2 = node.Node("Rocket")
node3 = node.Node("Groot")

node_list = [node1]

print(len(node_list))

print(node_list[0].get_name())

node_list.append(node2)

# print(node_list[1].get_name())

node_list[1] = node3

print(node_list[1].get_name())

node_list.append(node2)

c1 = node.Camp("Archery", "use bow and arrow", 100.23)
n1 = node.Node(c1)

print("printing in a for loop")
for x in node_list:
    print(x.get_name())
