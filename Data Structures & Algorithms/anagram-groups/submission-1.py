class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for i in strs:
            anag = "".join(sorted(i))
            print(anag)
            if anag in hash_map:
                hash_map[anag].append(i)
            else:
                hash_map[anag] = [i]
        return list(hash_map.values())
