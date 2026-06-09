class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # the maximum and minimum values 
        max_val = max(nums)
        min_val = min(nums)
        
        # maximum value of any subarray is max_val - min_val
        return (max_val - min_val) * k
