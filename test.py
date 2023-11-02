from graphviz import Source
from graph import Node, Graph
from utils import GraphFormat
from algorithms import dijkstra

n1 = Node("Madrid")
n2 = Node("Barcelona")
n1.add_neighbour(n2, 100)
n2.add_neighbour(n1, 200)
print(n1)
print(n2)


g = Graph(set([n1, n2]))
print(g)


g = GraphFormat.read('examples/g1.txt')
print(g)
print(GraphFormat.write_dot(g))

print(g.get_edges())


s = Source(GraphFormat.write_dot(g, "box"), filename="test.gv", format="png")
s.view()


#g = GraphFormat.read('examples/mundial.txt')
#print(g)
#print(GraphFormat.write_dot(g))

#print(g.get_edges())

#s = Source(GraphFormat.write_dot(g, "box"), filename="test2.gv", format="png")
#s.view()



g = GraphFormat.read('examples/wall-e.txt')
print(g)
print(GraphFormat.write_dot(g))

print(g.get_edges())

s = Source(GraphFormat.write_dot(g, "box"), filename="test3.gv", format="png")
s.view()

min_length, path = dijkstra(g, 'H', 'D')
print([n.name for n in path], min_length)
