class UnionFind:

    def __init__(self, arr):
        self.roots = []
        for i in arr:
            self.roots[i] = i

    def findRoot(self, i):
        root = i
        while self.roots[root] != root:
            root = self.roots[root]
        while self.roots[i] != i:
            tmp = self.roots[i]
            self.roots[i] = root
            i = tmp
        return root

    def connected(self, p, q):
        return self.findRoot(p) == self.findRoot(q)

    def union(self, p, q):
        proot = self.findRoot(p)
        qroot = self.findRoot(q)
        self.roots[proot] = qroot
