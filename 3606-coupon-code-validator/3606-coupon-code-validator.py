class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        b = {"electronics":0,"grocery":1,"pharmacy":2,"restaurant":3}

        res = []
        for i in range(n):
            if fullmatch(r"[a-zA-Z0-9_]+", code[i]) and businessLine[i] in b and isActive[i]:
                res.append([code[i], businessLine[i]])
        res.sort()
        res.sort(key = lambda x: b[x[1]])
        
        out = []
        for a,b in res: out.append(a)
        return out