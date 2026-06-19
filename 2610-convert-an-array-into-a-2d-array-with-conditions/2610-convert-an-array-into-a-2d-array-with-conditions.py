class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        result = []
        
        for num, count in freq.items():
            for i in range(count):
                if i >= len(result):
                    result.append([])
                result[i].append(num)
        
        return result
