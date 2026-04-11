class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for char in s:
            if char.isalnum() == True:
                res.append(char.lower())
        
        i, j = 0, len(res) - 1
        while i < j:
            if res[i] != res[j]:
                return False
            else:
                i += 1
                j -= 1
        return True