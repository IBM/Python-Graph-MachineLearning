def numIslands(self, grid: List[List[str]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    
    def dfs(row,col):
        
        if row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] == "0":
            return
        else:
            grid[row][col] = "0"
            
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
            
            
        
    result = 0
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "1":
                dfs(row,col)
                result += 1
    
    return result

"""
Steps:-
iterate each cell and do dfs
check for conditions that row col in grid and the value is not 0
else set value to 0 and do dfs for top bottom left right
increment counter at base level

"""