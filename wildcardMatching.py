from matplotlib.style import available


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    s_idx = 0
    p_idx = 0
    match = 0
    starIdx = -1            
    while (s_idx < len(s)):
        # if found then increment
        if (p_idx < len(p) and (p[p_idx] == '?' or s[s_idx] == p[p_idx])):
            s_idx+=1
            p_idx+=1
            
        # if doesnt match and star found in pattern then set star index, set string index where match found, increment pattern index
        elif (p_idx < len(p) and p[p_idx] == '*'):
            starIdx = p_idx
            match = s_idx
            p_idx+=1
        
        #if pattern value is not star then go backfor star index found before and increment pattern index, increment string index from match
        elif starIdx != -1:
            p_idx = starIdx + 1
            match+=1
            s_idx = match
        else:
            
            return False
    #last condition to handle if pattern remaining element is *
    while (p_idx < len(p) and p[p_idx] == '*'):
        p_idx+=1

    return p_idx == len(p)

isMatch("abcabczzzde","*abc???de*")
print("test")
"a b c a b c z z z d e"
#          !
"* a b c ? ? ?  d e *"
#      !

# a a b
# * b

