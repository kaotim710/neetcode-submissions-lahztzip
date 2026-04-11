class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            curr.add(s[r])
            res = max(r - l + 1, res)
        return res