from typing import Set, Dict
from graph import Node, Graph


def find_min_not_in_s(L: Dict[Node, float], S: Set[Node]) -> str:
    minL = float('inf')
    minNode = None
    for k in L:
        if L[k] < minL and k not in S:
            minL = L[k]
            minNode = k
    return minNode

def dijkstra(graph: Graph, src: str, dst: str) -> None:
    name2node = {n.name: n for n in graph.nodes}
    # Get src and dst nodes:
    src = name2node[src]
    dst = name2node[dst]
    n = len(graph.nodes)
    L = {n: float('inf') for n in graph.nodes}
    L[src] = 0
    path = {src: [src]}
    S = set()
    while dst not in S:
        u = find_min_not_in_s(L, S)
        S.add(u)
        for v, w in u.neighbours:
            if v not in S and L[u] + w < L[v]:
                L[v] = L[u] + w
                path[v] = path[u] + [v]
    return L[dst], path[dst]
