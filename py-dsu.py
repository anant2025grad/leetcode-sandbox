# union-find / disjoint set union
# used to manage collection of non-overlapping sets
# highly efficient for checking if elements belong
# to the same group and merging groups together


class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1] * n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]] # path halving
            x = self.p[x]
    return x

def union(self, a, b):
    a, b = self.find(a), self.find(b)
    if a == b: return False
    if self.sz[a] < self.sz[b]:
        a, b = b, a
    self.p[b] = a
    self.sz[a] += self.sz[b]
    return True 