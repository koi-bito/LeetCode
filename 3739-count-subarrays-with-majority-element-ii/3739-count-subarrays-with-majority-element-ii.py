from typing import List
from collections import defaultdict

class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)
    
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
    
    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        arr = [1 if num == target else -1 for num in nums]
        
        pref = [0]
        for x in arr:
            pref.append(pref[-1] + x)
        
        sorted_prefs = sorted(set(pref))
        index_map = {v: i + 1 for i, v in enumerate(sorted_prefs)}
        fenwick = FenwickTree(len(sorted_prefs))
        
        ans = 0
        for p in pref:
            idx = index_map[p]
            ans += fenwick.query(idx - 1)
            fenwick.update(idx, 1)
        
        return ans
