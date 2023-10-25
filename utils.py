import re
from enum import Enum
from graph import Node, Graph

class FormatParseError(Exception):
    """Exception for parsing problems."""

class GraphFormat():
    """
    Read and write graphs.
    """

    class ReadMode(Enum):
        TYPE = 1
        NODE = 2
        EDGE = 3

    @classmethod
    def read(cls, fname: str) -> Graph:
        re_comment = re.compile(r"\s*#\.*")
        re_empty = re.compile(r"\s*")
        re_node = re.compile(r"\s*(\w+)\s*")
        re_edge = re.compile(r"\s*(\w+)\s*::\s*(\w+)\s*")
        re_type_directed = re.compile(r"\s*directed\s*")
        
        read_mode = cls.ReadMode.TYPE

        nodes = []
        directed = False
        
        with open(fname, 'r') as f:
            for i, line in enumerate(f):
                if re_comment.fullmatch(line) or re_empty.fullmatch(line):
                    continue

                if read_mode == cls.ReadMode.TYPE:
                    match = re_type_directed.fullmatch(line)
                    if match:
                        directed = True
                        continue
                    read_mode = cls.ReadMode.NODE

                if read_mode == cls.ReadMode.NODE:
                    match = re_node.fullmatch(line)
                    if match:
                        name = match.groups()[0]
                        nodes.append(Node(name))
                        continue
                    graph = Graph(set(nodes), directed)
                    name2node = {n.name: n for n in graph.nodes}
                    read_mode = cls.ReadMode.EDGE

                if read_mode == cls.ReadMode.EDGE: 
                    match = re_edge.fullmatch(line)
                    if match:
                        n0 = name2node[match.groups()[0]]
                        n1 = name2node[match.groups()[1]]
                        n0.add_neighbour(n1)
                        if not directed:
                            n1.add_neighbour(n0)
                        continue
                    
                raise FormatParseError(f"Invalid expression in line {i+1}: {line}")

        return graph

    def write_dot(graph: Graph) -> str:
        return (
            "graph {\n"
            "  rankdir=LR;\n"
            "\n"
            + "".join(
                f"  {node.name}[shape=circle]\n"
                for node in graph.nodes
            )
            + "\n"
            + "".join(
                f"  {node0.name} -- {node1.name}\n"
            #    f"[label=\"{symbol_repr(t.symbol)}\"]\n"
                for node0 in graph.nodes for node1 in node0.neighbours
            )
            + "}\n"
        )

