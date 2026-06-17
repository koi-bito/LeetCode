class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        length = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = length[i]
            if ch == '*':
                length[i + 1] = cur - 1 if cur > 0 else 0
            elif ch == '#':
                length[i + 1] = cur * 2
            elif ch == '%':
                length[i + 1] = cur
            else:
                length[i + 1] = cur + 1

        if k >= length[-1]:
            return '.'

        pos = k
        for i in range(n - 1, -1, -1):
            ch = s[i]
            before = length[i]

            if ch == '*':
                continue
            elif ch == '#':
                if before > 0:
                    pos %= before
            elif ch == '%':
                pos = before - 1 - pos
            else:
                if pos == before:
                    return ch

        return '.'
