import re
from typing import Set

class FormatParseError(Exception):
    """Exception for parsing problems."""

class Node():
    """
    A graph's node.

    Args:
        name: node's name.
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.neighbours = []

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.name == other.name

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}({self.name!r}, neighbours={[x.name for x in self.neighbours]!r})"
        )

    def __hash__(self) -> int:
        return hash(self.name)

    def add_neighbour(self, n: 'Node') -> None:
        self.neighbours.append(n)


class Graph():
    """
    A graph is simply a set of nodes.

    Args:
        nodes: set of nodes.
    """
    def __init__(self, nodes: Set = set()) -> None:
        self.nodes = nodes

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.nodes == other.nodes

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(nodes={self.nodes!r})"
        )
        
    def add_nodes(self, nodes: Set[Node]) -> None:
        self.nodes |= nodes

    def read(fname: str) -> 'Graph':
        re_comment = re.compile(r"\s*#\.*")
        re_empty = re.compile(r"\s*")
        re_node = re.compile(r"\s*(\w+)\s*")
        re_undirected_edge = re.compile(r"\s*(\w+)\s*::\s*(\w+)\s*")
        re_directed_edge = re.compile(r"\s*(\w+)\s*>>\s*(\w+)\s*")

        reading_nodes = True
        reading_edges = False

        nodes = []
        
        with open(fname, 'r') as f:
            for i, line in enumerate(f):
                if re_comment.fullmatch(line) or re_empty.fullmatch(line):
                    continue

                if reading_nodes:
                    match = re_node.fullmatch(line)
                    if match:
                        name = match.groups()[0]
                        print(name)
                        nodes.append(Node(name))
                        continue

                    if re_undirected_edge.fullmatch(line) or re_directed_edge.fullmatch(line):
                        reading_nodes = False
                        reading_edges = True
                        graph = Graph(set(nodes))
                        name2node = {n.name: n for n in graph.nodes}
                        print(name2node)

                if reading_edges:
                    match = re_undirected_edge.fullmatch(line)
                    if match:
                        n0 = name2node[match.groups()[0]]
                        n1 = name2node[match.groups()[1]]
                        print(f"{n0.name} :: {n1.name}")
                        n0.add_neighbour(n1)
                        n1.add_neighbour(n0)
                        continue
                    
                    match = re_directed_edge.fullmatch(line)
                    if match:
                        n0 = name2node[match.groups()[0]]
                        n1 = name2node[match.groups()[1]]
                        print(f"{n0.name} >> {n1.name}")
                        n0.add_neighbour(n1)
                        continue
                    
                raise FormatParseError(f"Invalid expression in line {i+1}: {line}")

        return graph
                    
    def to_dot(fname: str) -> None:
        # To do...
        pass

    def adjacency_matrix(self) -> None:
        # To do...
        # Only if num nodes small
        pass

    def num_nodes(self) -> int:
        # To do...
        # Only if num nodes small
        pass

    def num_edges(self) -> int:
        # To do...
        # Only if num nodes small
        pass
