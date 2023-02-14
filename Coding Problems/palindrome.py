class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(x.lower() for x in s if x.isalnum())
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
    
"""
Steps:-
check if alnum and change to lower
set left and right pointer
if left != right then return false 
else increment l and decrement r

"""