class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        restricted = [float('inf')] * n
        for idx, max_val in restrictions:
            restricted[idx] = max_val
        
        max_from_left = [0] * n
        for i in range(1, n):
            max_from_left[i] = min(restricted[i], max_from_left[i-1] + diff[i-1])
        
        max_from_right = [0] * n
        max_from_right[n-1] = max_from_left[n-1]
        
        for i in range(n-2, -1, -1):
            max_from_right[i] = min(restricted[i], max_from_right[i+1] + diff[i])
        
        result = [min(max_from_left[i], max_from_right[i]) for i in range(n)]
        
        return max(result)
