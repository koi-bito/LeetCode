class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # Find the maximum and minimum values in the array
        max_val = max(nums)
        min_val = min(nums)
        
        # The maximum value of any subarray is max_val - min_val
        # Since we can choose the same subarray k times, the total value is:
        return (max_val - min_val) * k
