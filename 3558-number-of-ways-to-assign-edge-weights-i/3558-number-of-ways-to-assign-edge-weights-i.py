from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # adjacency list 
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # maximum depth using BFS
        max_depth = 0

        queue = deque()
        queue.append((1, 0)) #(current_node, current_depth)
        visited = set()
        visited.add(1)
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
        
        if max_depth == 0:
            return 0  # no edges 
        
        # 2^(max_depth - 1) mod (10^9 + 7)
        return pow(2, max_depth - 1, MOD)
