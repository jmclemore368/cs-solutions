# https://leetcode.com/problems/number-of-islands/


class Solution(object):
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_islands = 0
        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                if char == '1':  # Island
                    num_islands += 1
                    self.breadthFirstSearch(grid, i, j)
        return num_islands
        
    def breadthFirstSearch(self, grid, i, j):
        q = collections.deque()
        grid[i][j] = '-1'
        q.append((i, j))
        while q:
            # Indices to check
            i, j = q.popleft()
            
             # Add above
            if (i-1) >= 0 and grid[i-1][j] == '1':
                q.append((i-1,j))
                grid[i-1][j] = '-1'
                
            # Add below
            if (i+1) < len(grid) and grid[i+1][j] == '1':   
                q.append((i+1,j))
                grid[i+1][j] = '-1'
                  
            # Add left  
            if (j-1) >= 0 and grid[i][j-1] == '1':  
                q.append((i,j-1))
                grid[i][j-1] = '-1'
                
            # Add right
            if (j+1) < len(grid[i]) and grid[i][j+1] == '1':
                q.append((i,j+1))
                grid[i][j+1] = '-1'
            
        
