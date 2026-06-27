class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        from collections import Counter
        freq = Counter(nums)
        
        max_length = 1
        
        if 1 in freq:
            count_ones = freq[1]
            if count_ones % 2 == 1:
                max_length = max(max_length, count_ones)
            else:
                max_length = max(max_length, count_ones - 1)
        
        for num in freq:
            if num == 1:
                continue
                
            current = num
            length = 0
            
            while current in freq and freq[current] >= 2:
                length += 1
                current = current * current
            
            if current in freq and freq[current] >= 1:
                max_length = max(max_length, 2 * length + 1)
            else:
                if length > 0:
                    max_length = max(max_length, 2 * (length - 1) + 1)
        
        return max_length
