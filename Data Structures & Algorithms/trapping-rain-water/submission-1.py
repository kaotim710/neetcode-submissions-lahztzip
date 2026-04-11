class Solution:
    def trap(self, height: List[int]) -> int:
        curr_vol = 0
        total_vol = 0

        for i in range(len(height)):
            l_max = 0
            r_max = 0

            for l in range(i, -1, -1):
                l_max = max(height[l], l_max)
            
            for r in range(i, len(height)):
                r_max = max(height[r], r_max)
            
            total_vol += min(l_max, r_max) - height[i]
        return total_vol
                