class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        import math
        n = len(nums)
        
        # sparse tables
        log_n = int(math.log2(n)) + 1
        max_st = [[0] * log_n for _ in range(n)]
        min_st = [[0] * log_n for _ in range(n)]
        
        for i in range(n):
            max_st[i][0] = min_st[i][0] = nums[i]
            
        for j in range(1, log_n):
            for i in range(n - (1 << j) + 1):
                max_st[i][j] = max(max_st[i][j-1], max_st[i + (1 << (j-1))][j-1])
                min_st[i][j] = min(min_st[i][j-1], min_st[i + (1 << (j-1))][j-1])
        
        def query(l, r):
            length = r - l + 1
            k = int(math.log2(length))
            max_val = max(max_st[l][k], max_st[r - (1 << k) + 1][k])
            min_val = min(min_st[l][k], min_st[r - (1 << k) + 1][k])
            return max_val - min_val
        
        # max heap approach
        import heapq
        heap = [(-query(i, n-1), i, n-1) for i in range(n)]
        heapq.heapify(heap)
        
        res = 0
        for _ in range(k):
            val, l, r = heapq.heappop(heap)
            res -= val  # val is negative
            if r > l:
                heapq.heappush(heap, (-query(l, r-1), l, r-1))
                
        return res
