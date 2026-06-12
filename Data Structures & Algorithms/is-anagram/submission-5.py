class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = sorted(s)
        tlist = sorted(t)
        if len(s) != len(t):
            return False
        for a, b in zip(slist, tlist):
            if a != b:
                return False
        return True