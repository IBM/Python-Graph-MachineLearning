class triNode:
    def __init__(this):
        this.children = {}
        this.end = False
    
    def add(this,word):
        node = this
        for c in word:
            if c not in node.children:
                node.children[c] = triNode()
            node = node.children[c]
        node.end = True 
        
def findWords(board,words):
    ROWS = len(board)
    COLS = len(board[0])
    
    def dfs(node,r,c,result,word):
        if r < 0 or c < 0 or r == ROWS or c == COLS:
            return 
        if board[r][c] not in node.children or (r,c) in visit:
            return

        visit.add((r,c))
        node = node.children[board[r][c]]
        word += board[r][c]
        if node.end == True:
            result.append(word)
        dfs(node,r+1,c,result,word)
        dfs(node,r-1,c,result,word)
        dfs(node,r,c+1,result,word)
        dfs(node,r,c-1,result,word)
        
        visit.remove((r,c))
        
    root = triNode()
    for wrd in words:
         root.add(wrd)
    visit = set()
    result = []
    for row in range(ROWS):
        for col in range(COLS):
            #
            dfs(root,row,col,result,"")
    print(result)
    
    

        
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# ["oath","pea","eat","rain"]

findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])

"""
Create trie node
dfs every cell value
if i == len(word) return true
check for overflow conditions or if letter in word not in board or already visited, return false
else check in children, add to path and do dfs for top bottom left right with or condition, increment i
after completion remove that char from path
return result
"""