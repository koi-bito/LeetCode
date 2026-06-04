class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        
        min_L = min(landStartTime[i] + landDuration[i] for i in range(n))
        
        case1 = float('inf')
        for j in range(m):
            S = waterStartTime[j]
            D = waterDuration[j]
            if min_L <= S:
                candidate = S + D
            else:
                candidate = min_L + D
            if candidate < case1:
                case1 = candidate
        
        min_W = min(waterStartTime[j] + waterDuration[j] for j in range(m))
        
        case2 = float('inf')
        for i in range(n):
            L = landStartTime[i] + landDuration[i]
            d = landDuration[i]
            candidate = max(L, min_W + d)
            if candidate < case2:
                case2 = candidate
        
        return min(case1, case2)
