a = [[0 for i in range(4)] for j in range(4)]
#print(a)

a = [[0, 4, 0, 0],
 [1, 0, 0, 0], 
 [2, 0, 0, 0], 
 [3, 0, 0, 0]]

for col in range(len(a[0])):
    for row in range(len(a)):
        print(a[row][col])
