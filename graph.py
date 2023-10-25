from typing import Set

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
