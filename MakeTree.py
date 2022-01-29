class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next


n1 = Node(23)
n2 = Node(233)
n3 = Node(2334)

n1.set_next(n2)
n2.set_next(n3)

NodeList = []

n = n1
print("while")

while n is not None:
    print(n.get_value())
    NodeList.append(n)
    n = n.next

element1 = NodeList[0]

print(element1.get_value())

for x in NodeList:
    print("Value", x.get_value())
