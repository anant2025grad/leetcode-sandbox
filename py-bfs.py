# BFS (Breadth-first search)
# shortest path in unweighted graphs or grids

from collections import deque

def bfs(start, adj):
        dist = {start: 0}
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist