from typing import List

MOD = 10 ** 9 + 7

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp: List[List[int]] = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(2, n + 1):
            for i in range(1, n - length + 2): 
                j = i + length - 1
                best = float('inf')
                for k in range(i, j + 1):
                    left  = dp[i][k - 1]
                    right = dp[k + 1][j]
                    cost = k + max(left, right)
                    if cost < best:
                        best = cost
                dp[i][j] = best

        return dp[1][n]
