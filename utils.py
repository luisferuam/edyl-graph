import re
from graph import Node, Graph

class FormatParseError(Exception):
    """Exception for parsing problems."""

class GraphFormat():
    """
    Read and write graphs.
    """
    def read(fname: str) -> Graph:
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
                        nodes.append(Node(name))
                        continue

                    if re_undirected_edge.fullmatch(line) or re_directed_edge.fullmatch(line):
                        reading_nodes = False
                        reading_edges = True
                        graph = Graph(set(nodes))
                        name2node = {n.name: n for n in graph.nodes}

                if reading_edges:
                    match = re_undirected_edge.fullmatch(line)
                    if match:
                        n0 = name2node[match.groups()[0]]
                        n1 = name2node[match.groups()[1]]
                        n0.add_neighbour(n1)
                        n1.add_neighbour(n0)
                        continue
                    
                    match = re_directed_edge.fullmatch(line)
                    if match:
                        n0 = name2node[match.groups()[0]]
                        n1 = name2node[match.groups()[1]]
                        n0.add_neighbour(n1)
                        continue
                    
                raise FormatParseError(f"Invalid expression in line {i+1}: {line}")

        return graph

    def to_dot(fname: str) -> None:
        # To do...
        pass

