class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum_of_each = numbers[l] + numbers[r]
            if sum_of_each < target:
                l += 1
            elif sum_of_each > target:
                r -= 1
            else:
                return [l + 1, r + 1]