class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 1000000007
        n = len(edges) + 1
        
        # adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # depths and lifting table
        depth = [0] * (n + 1)
        up = [[0] * 20 for _ in range(n + 1)]
        
        def dfs(v, p, d):
            depth[v] = d
            up[v][0] = p
            for u in adj[v]:
                if u != p:
                    dfs(u, v, d + 1)
        
        dfs(1, 0, 0)
        
        for j in range(1, 20):
            for i in range(1, n + 1):
                if up[i][j-1]:
                    up[i][j] = up[up[i][j-1]][j-1]
        
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(20):
                if diff & (1 << i):
                    u = up[u][i]
            if u == v:
                return u
            for i in range(19, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]
        
        def path_length(u, v):
            if u == v:
                return 0
            l = lca(u, v)
            return depth[u] + depth[v] - 2 * depth[l]
        
        result = []
        for u, v in queries:
            k = path_length(u, v)
            if k == 0:
                result.append(0)
            else:
                result.append(pow(2, k - 1, MOD))
        return result
