class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # 題目大意為每一格到最近treasure的距離，中間會有water cell擋住
        # 從寶箱思考，利用bfs去更新鄰近的 cell

        rows, cols = len(grid), len(grid[0])
        visited = set() # 紀錄已探訪過的 land cell
        q = deque()
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        # update min for each of the element
        def update(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == -1:
                return
            if (r, c) in visited:
                return
            visited.add((r, c))
            q.append((r, c))
                

        dist = 0 
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                update(r + 1, c)
                update(r - 1, c)
                update(r, c + 1)
                update(r, c - 1)
            dist += 1        
