class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)   # pair: [temp, index]
        
        for i, n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append((n, i))
        return res