class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow, fast = 0, 1
        total = 0
        while fast < len(prices):
            if prices[slow] < prices[fast]:
                total = max(total, prices[fast] - prices[slow])
            else:
                slow = fast
            fast += 1
        return total