class Solution:
    def __init__(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = []
        for row in range(0,len(matrix)):
            for col in range(0,len(matrix[row])):
                if matrix[row][col] == 0 and (row,col) not in visited:
                    visited.append((row,col))
        
        print(matrix)
        for i in visited:
            print(i)
            self.update(i[0],i[1],matrix)
    
    def update(self,row,col,matrix):
        while row > 0:
            row -= 1
            matrix[row][col] = 0
            
        while row < len(matrix)-1:
            row +=1
            matrix[row][col] = 0
            
        while col > 0:
            col -= 1    
            matrix[row][col] = 0
            
        while row < len(matrix[0])-1:
            col += 1
            matrix[row][col] = 0     
                  
    
    def updateRowToZero(self,row,col,visited,matrix):
        if (row,col) not in visited:
            visited.append((row,col))
            matrix[row][col] = 0

            if row - 1 >= 0:
                self.updateRowToZero(row-1,col,visited,matrix)

            if row + 1 <= len(matrix)-1:
                self.updateRowToZero(row+1,col,visited,matrix)
                
    def updateColToZero(self,row,col,visited,matrix):
        if (row,col) not in visited:                
            if col - 1 >= 0:
                self.updateColToZero(row,col-1,visited,matrix)

            if col + 1 <= len(matrix[row])-1:
                self.updateColToZero(row,col+1,visited,matrix)

Solution([[1,1,1],
          [1,0,1],
          [1,1,1]])