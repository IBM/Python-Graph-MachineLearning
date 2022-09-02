class Solution:
    from collections import defaultdict
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = defaultdict(list)
        for i in words:
            if i in dic.keys():
                dic[i] +=1
            else:
                dic[i] = 1
        
        result = defaultdict(list)
        for j in dic.keys():
            
            result[dic[j]].append(j)
        keys = list(result.keys())
        print(keys)
        keys.sort(reverse=True)
        sol = []
        print(keys)
        for i in keys:
            for j in sorted(result[i]):
                
                sol.append(j)
                
        #sol.sort() 
        return sol[0:k]

"""
Steps:-
hashmap to get count of each char
set value as key and key as value
sort reverse true

"""