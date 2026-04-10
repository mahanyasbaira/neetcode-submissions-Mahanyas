class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
 # strings s and t so ex: mug = gum which is true 
        if len(s) != len(t):
            return False
        
        count_Str_S, count_Str_T = {}, {}

        for i in range(len(s)):
            count_Str_S[s[i]] = 1 + count_Str_S.get(s[i], 0)
            count_Str_T[t[i]] = 1 + count_Str_T.get(t[i], 0)
        for c in count_Str_S:
            if count_Str_S[c] != count_Str_T.get(c, 0):
                return False
        return True