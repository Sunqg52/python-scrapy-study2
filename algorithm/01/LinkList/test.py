from Node import Node
from linkList import linkList

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)

link = linkList()
for node in [Node1, Node2, Node3]:
	link.add_node(node)
link.print_link()