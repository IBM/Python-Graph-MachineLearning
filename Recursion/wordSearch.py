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
        
def exist(self, board, word: str) -> bool:
    rows, cols = len(board), len(board[0])
    path = set()
    
    def dfs(r, c, i):
        if i == len(word):
            return True
        if (min(r, c) < 0 or r >= rows or c >= cols or
            word[i] != board[r][c] or (r, c) in path):
            return False
        path.add((r, c))
        res = (dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1))
        path.remove((r, c))
        return res
    
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0): return True
    return False


#ans = findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"] )
#print(ans)
        

"""
Steps:-
dfs every cell value
if i == len(word) return true
check for overflow conditions or if letter in word not in board or already visited, return false
else add to path and do dfs for top bottom left right with or condition, increment i
after completion remove that char from path
return result

"""