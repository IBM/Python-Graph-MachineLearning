class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=set(s)
        for i in s:
            if i in a:
                a.remove(i)
                if s.count(i) == 1:
                    return s.index(i)  
        return -1