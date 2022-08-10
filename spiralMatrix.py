class Solution:
    def spiralOrder(self, matrix):
        visited = []
        result = []
        self.dfs(matrix,0,0,visited,result)
        
        return result
        
    def dfs(self,grid,row,col,visited,result):
        if (row,col) in visited:
            return
        visited.append((row,col))
        
        result.append(grid[row][col])
        if col+1 <= len(grid[0]) -1:
            self.dfs(grid,row,col+1,visited,result)
        if row+1 <= len(grid)-1:
            self.dfs(grid,row+1,col,visited,result)
        if col-1 >= 0:
            self.dfs(grid,row,col-1,visited,result)
        while row-1 >= 1 and (row-1,col) not in visited:
            visited.append((row-1,col))
            result.append(grid[row-1][col])
            row -= 1
        if col+1 <= len(grid[0]) -1:
            self.dfs(grid,row,col+1,visited,result)        

sol = Solution()
sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])

