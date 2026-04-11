class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for i, n in enumerate(nums):
            if n in hash_map:   return True
            hash_map[n] = 1
        return False