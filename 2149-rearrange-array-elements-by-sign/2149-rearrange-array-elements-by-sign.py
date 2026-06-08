from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Step 1: Separate positive and negative numbers
        positive = []
        negative = []

        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)

        # Step 2: Merge the two lists alternately
        result = []
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])

        return result
