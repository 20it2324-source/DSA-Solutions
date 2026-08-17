class Solution:
    
    def countIslands(self, grid):
        # code here
        n, m = len(grid), len(grid[0])
        visited = [[False]*m for _ in range(n)]

        directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

        def dfs(x, y):
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 'L':
                    dfs(nx, ny)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L' and not visited[i][j]:
                    dfs(i, j)
                    count += 1

        return count
