class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 這題本質是在找是不是no cycle（無環）以及 每個點都相連通
        # 太多邊的情況，因為題目已說 n - 1個邊
        if len(edges) > n - 1:
            return False
        
        # 創建adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:  # 因為是undirected，所以兩邊都要補上相鄰的node
            adj[u].append(v)
            adj[v].append(u)
        visited = set() # 用來檢查cycle 以及確認所有點都被visited
        
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
        