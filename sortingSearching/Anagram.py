class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = collections.defaultdict(int)
        for n1 in s:
            hash_map[n1]+=1
        for n2 in t:
            if n2 in hash_map:
                hash_map[n2]-=1
            else:
                hash_map[n2]+=1
        return max(hash_map.values()) == 0

"""
Steps:-
get count for each value and store in hashmap
remove values from hashmap if presernt in target else add
return max of hashmapvalue and check if 0

"""