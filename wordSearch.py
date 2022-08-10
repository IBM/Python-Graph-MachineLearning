# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.end = False
    
#     def add_word(self, word):
#         node = self
#         for c in word:
#             if c not in node.children:
#                 node.children[c] = TrieNode()
#             node = node.children[c]
#         node.end = True
        
class TrieNode:
    def __init__(this):
        this.children = {}
        this.end = False

    def add_word(this,word):
        node = this
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

def findWords( board, words):
    root = TrieNode()
    for w in words:
        root.add_word(w)
    
    rows, cols = len(board), len(board[0])
    ans = []
    word = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def dfs(x, y, node):
        if not (0 <= x < rows) or not (0 <= y < cols) or board[x][y] == "#":
            return
        
        char = board[x][y]
        if char not in node.children:
            return

        board[x][y] = "#"
        
        node = node.children[char]
        word.append(char)
        if node.end:
            ans.append("".join(word))
            node.end = False
        
        for dx, dy in directions:
            dfs(x + dx, y + dy, node)
        
        word.pop()
        board[x][y] = char
    
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, root)
    
    return ans

ans = findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"] )
print(ans)
        

