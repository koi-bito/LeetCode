from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        """
        returns sum of waviness over all numbers in [num1, num2] (inclusive)
        """
        # helper: total waviness of all numbers 0 .. N
        def pref(N: int) -> int:
            if N < 0:
                return 0
            s = str(N)
            digits = list(map(int, s))
            n = len(digits)

            @lru_cache(maxsize=None)
            def dfs(pos: int, tight: bool, started: bool,
                    prev1: int, prev2: int):
                """
                returns (cnt, total_wav) for the suffix starting at position pos
                """
                if pos == n: # all positions processed
                    # one concrete number (maybe 0) is formed
                    return (1, 0)

                limit = digits[pos] if tight else 9
                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    # still in leading zeros ?
                    if not started and d == 0:
                        cnt, wav = dfs(pos + 1, ntight, False, -1, -1)
                        total_cnt += cnt
                        total_wav += wav
                        continue

                    # we place a real digit now
                    if not started:   # this is the first real digit
                        cnt, wav = dfs(pos + 1, ntight, True, d, -1)
                        total_cnt += cnt
                        total_wav += wav
                    else:
                        # we already have at least one real digit
                        add = 0
                        if prev2 != -1:   # we have three real digits now
                            if prev2 < prev1 and prev1 > d:
                                add = 1   # peak
                            elif prev2 > prev1 and prev1 < d:
                                add = 1          # valley
                        cnt, wav = dfs(pos + 1, ntight, True, d, prev1)
                        total_cnt += cnt
                        total_wav += wav + add * cnt

                return (total_cnt, total_wav)

            # the second component is the wanted sum
            _, total = dfs(0, True, False, -1, -1)
            return total

        # final answer = pref(num2) - pref(num1-1)
        return pref(num2) - pref(num1 - 1)
