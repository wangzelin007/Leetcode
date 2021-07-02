class Node:

    def __init__(self, v, i, o, n, e):
        self.value = v
        self.int = i # 直接进来几条 int
        self.out = o # 直接出去几条 int
        self.nexts = n # 直接出发相连的邻居 list
        self.edges = e # 直接出发的边 list

class Edge:

    def __init__(self, w, f, t):
        self._weight = w
        self._from = f
        self._to = t

class Graph:

    def __init__(self, nodes, edges):
        self.nodes = nodes # {id: node}
        self.edges = edges # set