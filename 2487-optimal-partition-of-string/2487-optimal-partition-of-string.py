class Solution:
    def partitionString(self, s: str) -> int:
        lookup = set()
        res = 1
        i = 0
        while i < len(s):
            if s[i] not in lookup:
                lookup.add(s[i])
                i += 1
            else:
                res += 1
                lookup.clear()
                lookup.add(s[i])
                i += 1
        return res
