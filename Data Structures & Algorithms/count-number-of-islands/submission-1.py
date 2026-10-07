class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        been = set() # (r, c) 
        islands = 0
        q = deque()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            been.add((r, c))
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if (0 <= newR < len(grid) and
                        0 <= newC < len(grid[0]) and
                        grid[newR][newC] == '1' and
                        (newR, newC) not in been):
                        q.append((newR, newC))
                        been.add((newR, newC))
                    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in been:
                    bfs(r, c)
                    islands += 1
        
        return islands

        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        """if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == "1" and 
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands"""
            
