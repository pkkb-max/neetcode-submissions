class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['{','(','[']
        closing = ['}',')',']']
        res = []
        for char in s:
            if char in opening:
                res.append(char)
            elif len(res) == 0 or char not in closing:
                return False
            elif res[-1] == opening[closing.index(char)]:
                res.pop()
            else:
                return False
        if len(res) == 0:
            return True
        return False
