


def wildCardMatching(s,p):
    
    s_idx = 0
    p_idx = 0
    match = 0
    star_idx = -1
    while s_idx < len(s):
        if s[s_idx] == p[p_idx] or p[p_idx] == "?" and p_idx < len(p):
             s_idx += 1
             p_idx += 1
             
        elif p[p_idx] == "*":
            star_idx = p_idx
            match = s_idx  
            p_idx += 1
        elif star_idx != -1:
            p_idx = star_idx + 1
            match += 1
            s_idx = match
        else:
            return False
    
    while p_idx < len(p) and p[p_idx] == "*":
        p_idx += 1
        
    return p_idx == len(p)
        
print(wildCardMatching("abcabczzzde","*abc???de*"))
            
#"a b c a b c z z z d e"
#                     !
#"* a b c ? ? ?  d e *"
#                  !