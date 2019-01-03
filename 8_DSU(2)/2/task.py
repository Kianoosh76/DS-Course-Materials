class Node(object):
    def __init__(self, label):
        self.label = label
        self.par = self
        self.rank = 0


class DisjointSet(object):
    def __init__(self, n):
        self.n = n
        self.nodes = [Node(i) for i in range(n)]

    def find(self, u):
        if u == u.par:
            return u
        return self.find(u.par)

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:  # u and v are in the same component
            return False

        # making v the vertex with better rank
        if u.rank > v.rank:
            u, v = v, u

        # merging two components
        u.par = v

        # updating maximum depth as rank
        if u.rank == v.rank:
            v.rank += 1

        return True

    # Returns a list of components where each component is a list of values
    def get_all_components(self):
        comps = [[] for _ in range(self.n)]
        for node in self.nodes:
            comps[self.find(node).label].append(node.label)

        comps = [i for i in comps if i]  # Remove empty lists
        return comps


def solve(n, a, b):
    dsu = DisjointSet(26)
    for i in range(n):
        n1 = dsu.nodes[ord(a[i]) - ord('a')]
        n2 = dsu.nodes[ord(b[i]) - ord('a')]
        dsu.union(n1, n2)
    comps = dsu.get_all_components()

    ans = 26 - len(comps)
    rules = []
    for i in comps:
        if len(i) > 1:
            for j in range(1, len(i)):
                rules.append((chr(ord('a') + i[0]), chr(ord('a') + i[j])))

    return ans, rules

