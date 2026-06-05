class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:                     # three non‑empty parts are impossible
            return 0

        # ---------- 1. build LCP ----------
        # LCP[p][q]  (0 ≤ p ≤ q ≤ n)   extra row/col n is all zeros
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for p in range(n - 1, -1, -1):
            for q in range(n - 1, p, -1):          # q > p
                if nums[p] == nums[q]:
                    lcp[p][q] = lcp[p + 1][q + 1] + 1

        # ---------- 2. count beautiful splits ----------
        ans = 0
        # i = last index of nums1, j = last index of nums2
        for i in range(0, n - 2):          # i ≤ n‑3
            len1 = i + 1
            for j in range(i + 1, n - 1):  # j ≤ n‑2
                len2 = j - i
                len3 = n - j - 1

                # condition A: nums1 is a prefix of nums2
                a = (len1 <= len2) and (lcp[0][i + 1] >= len1)

                # condition B: nums2 is a prefix of nums3
                b = (len2 <= len3) and (lcp[i + 1][j + 1] >= len2)

                if a or b:
                    ans += 1
        return ans
