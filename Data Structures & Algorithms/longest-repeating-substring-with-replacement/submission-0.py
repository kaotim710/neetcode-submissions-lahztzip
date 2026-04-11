class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 題目是要window裡面最好都同一個char
        window = {}
        l, r = 0, 0
        res = 0
        maxf = 0

        while r < len(s):
            # move in
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            maxf = max(window[c], maxf)
            
            while (r - l + 1) - maxf > k:
                window[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res