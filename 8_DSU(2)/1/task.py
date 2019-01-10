class Node(object):
    def __init__(self, label):
        self.label = label
        self.par = self
        self.size = 1
        self.sum = 0
        self.added = False


class DisjointSet(object):
    def __init__(self, n):
        self.n = n
        self.nodes = [Node(i) for i in range(n)]

    def find(self, u):
        if u != u.par:  # here we user path compression trick
            u.par = self.find(u.par)
        return u.par

    def unite(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:  # u and v are in the same component
            return False

        # making v the vertex with bigger size
        if u.size > v.size:
            u, v = v, u

        # merging two components
        u.par = v

        # updating necessary variables
        v.size += u.size
        v.sum += u.sum

        return True


def solve(n, numbers, perm):
    # numbers is a list of n integers
    # perm is a list of the numbers 1 to n in some permutation
    # Return a list of answers

    perm2 = [i - 1 for i in perm]
    perm = perm2
    answers = []
    current_answer = 0
    dsu = DisjointSet(n)

    def add(i, current_answer):
        node = dsu.nodes[i]
        node.added = True
        node.sum = numbers[i]
        if i > 0 and dsu.nodes[i - 1].added:
            dsu.unite(node, dsu.nodes[i - 1])
        if i < n - 1 and dsu.nodes[i + 1].added:
            dsu.unite(node, dsu.nodes[i + 1])

        parent = dsu.find(node)
        current_answer = max(current_answer, parent.sum)
        return current_answer

    for i in range(n - 1, -1, -1):
        answers.append(current_answer)
        current_answer = add(perm[i], current_answer)

    answers.reverse()
    return answers
