class Solution:
    def trap(self, height: List[int]) -> int:
        '''
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
        '''
        # 備忘錄方法
        l_max = [0] * len(height)
        r_max = [0] * len(height)
        res = 0

        l_max[0] = height[0]
        r_max[len(height) - 1] = height[len(height) - 1]
        
        # 計算l_max()
        for i in range(1, len(height)):
            l_max[i] = max(height[i], l_max[i - 1])
        # 計算r_max
        for i in range(len(height) - 2, -1, -1):
            r_max[i] = max(height[i], r_max[i + 1])

        # 得到i當下可以累積的水量並加總
        for i in range(1, len(height) - 1):
            res += min(l_max[i], r_max[i]) - height[i]
        return res
