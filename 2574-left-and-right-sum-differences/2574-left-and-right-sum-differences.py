from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        """
        Returns answer[i] = |sum(nums[0:i]) - sum(nums[i+1:])|
        for every index i.
        """
        total = sum(nums)   # sum of the whole array
        left = 0     # sum of elements left of the current index
        ans = []

        for x in nums:  # iterate through the array
            # right part = total - left - current element
            right = total - left - x
            ans.append(abs(left - right))
            left += x  # extend left part for the next position

        return ans
