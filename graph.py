from typing import Set, List

class Node():
    """
    A graph's node.
    Multiple edges are not allowed.

    Args:
        name: node's name.
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.neighbours = set()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.name == other.name

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}({self.name!r}, neighbours={[(x[0].name, x[1]) for x in self.neighbours]!r})"
        )

    def __hash__(self) -> int:
        return hash(self.name)

    def add_neighbour(self, n: 'Node', w: float) -> None:
        self.neighbours.add((n, w))
        

class Graph():
    """
    A graph is simply a set of nodes.

    Args:
        nodes: set of nodes.
        directed: boolean flag indicating that the graph is directed.
        weighted: boolean flag indicating that the graph is weighted.
    """
    def __init__(self, nodes: Set[Node] = set(), directed: bool = False, weighted: bool = False) -> None:
        self.nodes = nodes
        self.directed = directed
        self.weighted = weighted

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.nodes == other.nodes

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(directed={self.directed!r}, weighted={self.weighted!r}, nodes={self.nodes!r})"
        )
        
    def add_nodes(self, nodes: Set[Node]) -> None:
        self.nodes |= nodes

    def set_weighted(self, weighted: bool) -> None:
        self.weighted = weighted

    def get_edges(self) -> List[str]:
        if self.directed:
            edges = [(n0.name, n1.name, w) for n0 in self.nodes for (n1, w) in n0.neighbours]
        else:
            edges = set([tuple(sorted([n0.name, n1.name])+[w]) for n0 in self.nodes for (n1, w) in n0.neighbours])
        return edges
                    
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

    def is_connected(self) -> int:
        # To do...
        # Only if num nodes small
        pass
