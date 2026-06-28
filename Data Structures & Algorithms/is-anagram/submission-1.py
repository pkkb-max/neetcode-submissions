class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = {}
        for ch in s:
            if ch in smap:
                smap[ch]+=1
            else:
                smap[ch]=1
        for ch in t:
            if ch in smap:
                smap[ch]-=1
                if smap[ch] < 0:
                    return False
            else:
                return False
        return True
