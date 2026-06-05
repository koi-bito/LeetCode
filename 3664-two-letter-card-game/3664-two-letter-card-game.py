from typing import List
import heapq

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        # ------------------------------------------------------------
        # 1.  count the three kinds of cards
        # ------------------------------------------------------------
        ALPH = 10                     # letters a … j
        base = ord('a')
        cnt1 = [0] * ALPH            # x ?   (x in first position)
        cnt2 = [0] * ALPH            # ? x   (x in second position)
        both = 0                      # x x

        for s in cards:
            if x not in s:
                continue
            if s[0] == x and s[1] == x:
                both += 1
            elif s[0] == x:          # x ?
                idx = ord(s[1]) - base
                cnt1[idx] += 1
            else:                    # ? x
                idx = ord(s[0]) - base
                cnt2[idx] += 1

        # ------------------------------------------------------------
        # 2.  for a side: internal[k] = maximal internal pairs after
        #     removing exactly k ordinary cards (optimal deletions)
        # ------------------------------------------------------------
        def build_internal(cnt):
            total = sum(cnt)
            internal = [0] * (total + 1)          # internal[k]
            if total == 0:
                return internal

            # max‑heap of the frequencies (as negative numbers)
            heap = [-c for c in cnt if c > 0]
            heapq.heapify(heap)

            # 0 deletions
            mx = -heap[0]
            internal[0] = min(total // 2, total - mx)

            # delete cards one by one, always from the current largest colour
            for k in range(1, total + 1):
                top = -heapq.heappop(heap)       # largest frequency
                top -= 1                         # delete one card
                if top > 0:
                    heapq.heappush(heap, -top)

                remain = total - k
                if remain == 0:
                    internal[k] = 0
                else:
                    mx = -heap[0] if heap else 0
                    internal[k] = min(remain // 2, remain - mx)
            return internal

        internal1 = build_internal(cnt1)   # length total1+1
        internal2 = build_internal(cnt2)   # length total2+1
        total1 = sum(cnt1)
        total2 = sum(cnt2)

        # ------------------------------------------------------------
        # 3.  try every possible distribution of the wildcards
        # ------------------------------------------------------------
        ans = 0
        for i in range(both + 1):               # i wildcards to side 1
            use1 = min(i, total1)               # real pairs formed with side‑1
            score1 = use1 + internal1[use1]

            use2 = min(both - i, total2)
            score2 = use2 + internal2[use2]

            ans = max(ans, score1 + score2)

        return ans
