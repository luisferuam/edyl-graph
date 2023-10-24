from graph import Node, Graph

n1 = Node("Madrid")
n2 = Node("Barcelona")
n1.add_neighbour(n2)
n2.add_neighbour(n1)
print(n1)
print(n2)


g = Graph(set([n1, n2]))
print(g)


g = Graph.read('g1.txt')
print(g)
