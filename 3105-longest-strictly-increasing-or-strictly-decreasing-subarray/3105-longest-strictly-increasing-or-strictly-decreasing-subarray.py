class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        max_increasing = 1
        max_decreasing = 1
        
        current_increasing = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_increasing += 1
                max_increasing = max(max_increasing, current_increasing)
            else:
                current_increasing = 1
        
        current_decreasing = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                current_decreasing += 1
                max_decreasing = max(max_decreasing, current_decreasing)
            else:
                current_decreasing = 1
        
        return max(max_increasing, max_decreasing)
