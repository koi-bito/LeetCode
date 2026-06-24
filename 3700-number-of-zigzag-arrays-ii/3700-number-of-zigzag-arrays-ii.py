import sys

MOD = 10 ** 9 + 7


class Solution:
    """
    Number of ZigZag arrays.
    The method follows exactly the algorithm proven correct above.
    """

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        if n == 1:
            return m % MOD

        sz = 2 * m

        T = [[0] * sz for _ in range(sz)]

        for x in range(m):

            for y in range(x):
                T[m + y][x] = 1 

            for y in range(x + 1, m):
                T[y][m + x] = 1

        def mat_mul(A, B):
            n = len(A)
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                Ai = A[i]
                Ci = C[i]
                for k in range(n):
                    aik = Ai[k]
                    if aik:
                        Bk = B[k]
                        for j in range(n):
                            Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
            return C

        def mat_pow(A, power):
            n = len(A)
            res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            while power:
                if power & 1:
                    res = mat_mul(res, A)
                A = mat_mul(A, A)
                power >>= 1
            return res

        T_pow = mat_pow(T, n - 1)

        ans = 0
        for row in T_pow:
            ans = (ans + sum(row)) % MOD
        return ans
