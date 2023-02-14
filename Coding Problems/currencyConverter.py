from collections import deque
def ConvertCurrency(cur1,cur2,graph):
    visited = []
    q = deque([(cur1,1.0)])
    while q:
        
        currency,val = q.popleft()
        if currency not in visited:
            visited.append(currency)
            
        if currency == cur2:
            return val
        

        for i in graph[currency]:
            currencyChild,valChild = i
            if currencyChild not in visited:
                valChild = val * valChild
                q.append((currencyChild,valChild))