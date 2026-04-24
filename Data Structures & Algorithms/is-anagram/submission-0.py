class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sChar = {}
        tChar = {}

        for c in s:
            if c not in sChar:
                sChar[c] = 1
            else:
                sChar[c] += 1
        for c in t:
            if c not in tChar:
                tChar[c] = 1
            else:
                tChar[c] += 1
        
        return sChar == tChar