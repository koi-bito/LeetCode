import sys

MOD = 10 ** 9 + 7

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        
        m = r - l + 1

        dp_up   = [1] * m
        dp_down = [1] * m

        for _ in range(1, n):

            pref_up = [0] * m
            cur = 0
            for i in range(m):
                cur = (cur + dp_up[i]) % MOD
                pref_up[i] = cur

            pref_down = [0] * m
            cur = 0
            for i in range(m):
                cur = (cur + dp_down[i]) % MOD
                pref_down[i] = cur
            total_down = cur

            new_up   = [0] * m
            new_down = [0] * m
            for i in range(m):
                new_up[i] = (total_down - pref_down[i]) % MOD

                new_down[i] = pref_up[i - 1] if i > 0 else 0

            dp_up, dp_down = new_up, new_down

        ans = (sum(dp_up) + sum(dp_down)) % MOD
        return ans
