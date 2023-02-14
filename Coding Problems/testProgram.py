from collections import defaultdict


dic = defaultdict(list)
dic["a"] = 1
dic['b'] = 2
print(dic)

del dic['a'] 
print(dic)

import heapq

arr = []

heapq.heappush(arr,9)
heapq.heappush(arr,19)
heapq.heappush(arr,5)
print(arr[0])

print([[0 for i in range(4)] for j in range(4)])

print(len([1,2,3,4])//2)

#There are n days of fruit price data. Find the minimum total price so the user can eat one fruit each day. 

#Followup q, if the fruits rot in d days, then get the total.


#EXPAND THESE
# 3[a] = aaa
# 3[a2[b]] = abbabbabb  => a2[b] + a2[b] + a2[b] => abb + abb + abb
# 2[cd] = cdcd


#3[a2[b]] = > 
#l      r

def expand(word):
    stack = []
    result = ""
    def backtrack(word,l,r):
        nonlocal stack
        l = 0
        r = len(word)
        if word == "":
            return stack
        if len(word) == 1:
            stack.append(word) 
            
        else:
            if word[l].isalnum():
                if word[l].isnumeric():
                    stack.append(int(word[l]))
                    
                    
                    backtrack(word[l+1:r+1],l,r)
                else:
                    str = ''
                    while l <= r and word[l].isalnum() and word[l].isnumeric() == False:
                        
                        str += word[l]
                        l+=1
                    l = min(l,len(word)-1)     
                    stack.append(str)
                        
                    backtrack(word[l:r],l,r)    
            else:
                l+=1
                r-=1
                backtrack(word[l:r],l,r)    
                
    backtrack(word,0,len(word)-1)
    result = ""
    while stack:
        val = stack.pop()
        if type(val) != int:
            result = val +result
        else:
            temp = result
            for i in range(val-1):
                result += temp
    print(result)
                
            
            
        
        
    print("finish")
  


#print(expand("3[a2[b]]"))
print(expand("2[cd]"))

 
#print("[".isalnum())