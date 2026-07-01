from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    queue.append((i, j, 0))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            x, y, d = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] > d + 1:
                    dist[nx][ny] = d + 1
                    queue.append((nx, ny, d + 1))
        
        def canReach(safeness):
            if dist[0][0] < safeness or dist[n-1][n-1] < safeness:
                return False
            
            visited = [[False] * n for _ in range(n)]
            queue = deque([(0, 0)])
            visited[0][0] = True
            
            while queue:
                x, y = queue.popleft()
                if x == n - 1 and y == n - 1:
                    return True
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < n and 0 <= ny < n and 
                        not visited[nx][ny] and dist[nx][ny] >= safeness):
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            
            return False
        
        left, right = 0, 2 * n - 2
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canReach(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
