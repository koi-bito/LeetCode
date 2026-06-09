import sys
from typing import List
from collections import defaultdict

sys.setrecursionlimit(1 << 25)

MOD = 10**9 + 7

class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        n = len(prevRoom)
        
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD
        
        # tree
        children = defaultdict(list)
        for i in range(1, n):
            children[prevRoom[i]].append(i)
        
        # DFS: compute subtree sizes and number of ways
        def dfs(u):
            size = 1
            ways = 1
            child_sizes = []
            
            for v in children[u]:
                child_size, child_ways = dfs(v)
                size += child_size
                ways = (ways * child_ways) % MOD
                child_sizes.append(child_size)
            
            # multinomial coefficient 
            total_child_size = sum(child_sizes)
            numerator = fact[total_child_size]
            denominator = 1
            for cs in child_sizes:
                denominator = (denominator * inv_fact[cs]) % MOD
            multinomial = (numerator * denominator) % MOD
            
            ways = (ways * multinomial) % MOD
            return size, ways
        
        _, result = dfs(0)
        return result
