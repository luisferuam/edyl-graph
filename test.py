from graphviz import Source
from graph import Node, Graph
from utils import GraphFormat

n1 = Node("Madrid")
n2 = Node("Barcelona")
n1.add_neighbour(n2)
n2.add_neighbour(n1)
print(n1)
print(n2)


g = Graph(set([n1, n2]))
print(g)


g = GraphFormat.read('g1.txt')
print(g)
print(GraphFormat.write_dot(g))

print(g.get_edges())


s = Source(GraphFormat.write_dot(g), filename="test.gv", format="png")
s.view()
