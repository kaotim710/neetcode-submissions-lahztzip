class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):    return False
        return True if Counter(s) == Counter(t) else False