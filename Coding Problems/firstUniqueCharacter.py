class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=set(s)
        for i in s:
            if i in a:
                a.remove(i)
                if s.count(i) == 1:
                    return s.index(i)  
        return -1

"""
Steps:-
Create a set of unique characters
if char in set then remove from set
if count is 1 then return 


"""

print("aabc".count("a"))