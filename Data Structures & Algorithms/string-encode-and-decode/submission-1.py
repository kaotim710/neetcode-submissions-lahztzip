class Solution:

    def encode(self, strs: List[str]) -> str:
        # attach each string with its length
        # hashtag as a delimiter
        
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        # 考慮十位數的情況
        while i < len(s):
            length = 0
            # meet hashtag才停
            while s[i] != '#':
                length = length * 10 + int(s[i])
                i += 1
            # skip hashtag
            i += 1
            
            # get the word
            word = s[i:i + length]
            res.append(word)
            
            # ptr move to next digit
            i += length
        return res