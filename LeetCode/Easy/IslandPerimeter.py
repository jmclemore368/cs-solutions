# https://leetcode.com/problems/island-perimeter/


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for x, row in enumerate(grid):
            for y, item in enumerate(row):
                # There is guaranteed to be one island. 
                # Once we find it, BFS will find all connected cells.
                # Thus, we can break afterwards as there's nothing left to explore.
                if grid[x][y] == 1:
                    perimeter += self.islandPerimeterBFS(grid, x, y)
                    break
        return perimeter
        
    def islandPerimeterBFS(self, grid, x, y):
        count = 0
        q = collections.deque()
        q.append((x, y))
        grid[x][y] = -1
        while q:
            # For each (x, y) that we are exploring, we check above, below, left, and right.
            # If out of bounds, increase count by 1.
            # else if 0, increase count by 1.
            # else if 1, add to queue to explore and mark visited.
            x, y = q.popleft()
            
            # Explore above
            if (x - 1) < 0: 
                count += 1
            elif (x - 1) >= 0 and grid[x - 1][y] == 0:
                count += 1
            elif (x - 1) >= 0 and grid[x - 1][y] == 1:
                q.append((x - 1, y))
                grid[x - 1][y] = -1
                
            # Explore below
            if (x + 1) > len(grid) - 1: 
                count += 1
            elif (x + 1) <= (len(grid) - 1) and grid[x + 1][y] == 0:
                count += 1
            elif (x + 1) <= (len(grid) - 1) and grid[x + 1][y] == 1:
                q.append((x + 1, y))
                grid[x + 1][y] = -1
            
            # Explore left
            if (y - 1) < 0: 
                count += 1
            elif (y - 1) >= 0 and grid[x][y - 1] == 0:
                count += 1
            elif (y - 1) >= 0 and grid[x][y - 1] == 1:
                q.append((x, y - 1))
                grid[x][y - 1] = -1

            # Explore right
            if (y + 1) > len(grid[x]) - 1: 
                count += 1
            elif (y + 1) <= (len(grid[x]) - 1) and grid[x][y + 1] == 0:
                count += 1
            elif (y + 1) <= (len(grid[x]) - 1) and grid[x][y + 1] == 1:
                q.append((x, y + 1))     
                grid[x][y + 1] = -1
                
        return count
            
            
            
