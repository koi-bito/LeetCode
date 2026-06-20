class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        
        restrictions.sort()
        
        for i in range(1, len(restrictions)):
            prev_id, prev_height = restrictions[i-1]
            curr_id, curr_height = restrictions[i]
            max_achievable = prev_height + (curr_id - prev_id)
            restrictions[i][1] = min(curr_height, max_achievable)
        
        for i in range(len(restrictions) - 2, -1, -1):
            next_id, next_height = restrictions[i+1]
            curr_id, curr_height = restrictions[i]
            max_needed = next_height + (next_id - curr_id)
            restrictions[i][1] = min(curr_height, max_needed)
        
        max_height = 0
        for i in range(len(restrictions) - 1):
            left_id, left_height = restrictions[i]
            right_id, right_height = restrictions[i+1]
            
            max_height = max(max_height, left_height, right_height)
            
            distance = right_id - left_id
            height_diff = abs(right_height - left_height)
            if distance > height_diff:
                extra = distance - height_diff
                peak_height = max(left_height, right_height) + extra // 2
                max_height = max(max_height, peak_height)
        
        return max_height
