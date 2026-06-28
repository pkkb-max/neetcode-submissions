class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_w = 0
        substr_ct = float('inf')
        substr= ""
        res = {}
        for left in range(len(t)):
            if t[left] not in res:
                res[t[left]] = 1
            else:
                res[t[left]] +=1
        for ch_ind in range(len(s)):
            if s[ch_ind] in res:
                start = ch_ind
                end = ch_ind
                curr = res.copy()
                while(end < len(s)):
                    if s[end] in curr:
                        curr[s[end]] -= 1
                        if curr[s[end]] == 0:
                            del curr[s[end]]
                    if len(curr) == 0:
                        break
                    end+=1
                if (substr == "" or len(substr) > len(s[start:end+1])) and len(curr) == 0:
                    substr = s[start:end+1]
        return substr
