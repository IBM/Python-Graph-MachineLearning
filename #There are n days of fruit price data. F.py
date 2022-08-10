#There are n days of fruit price data. Find the minimum total price so the user can eat one fruit each day. 

#Followup q, if the fruits rot in d days, then get the total.


#EXPAND THESE
# 3[a] = aaa
# 3[a2[b]] = abbabbabb  => a2[b] + a2[b] + a2[b] => abb + abb + abb
# 2[cd] = cdcd


#3[a2[b]]
#l      r  
def expand(word):
    l = 0
    r = len(word) - 1
    
    
    while l < r:
        if type(l) == int:
            print(l)
            
print(type(2))