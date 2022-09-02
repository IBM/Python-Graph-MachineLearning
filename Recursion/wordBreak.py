class Solution:
    from collections import deque
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([s])
        
        visited = []
        while q:
            s = q.popleft()
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if len(new_s) == 0:
                        return True
                    if new_s not in visited:
                        q.append(new_s)
                        visited.append(new_s)
        return False

"""
Steps:-
create queue and add word to it

while queue not empty pop queue and check it starts with word in inventory
if yes then create new word with other remaining letters
append that to queue 

"""