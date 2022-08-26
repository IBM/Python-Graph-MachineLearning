
from collections import defaultdict
def findTopK(arr,k):
    bucket = [[] for i in range(len(arr))]
    dicCount = defaultdict(int)

    for i in range(len(arr)):
        dicCount[arr[i]] += 1

    for n,c in dicCount.items():
        bucket[c].append(n)
    print(bucket)
   
    res = []
    for i in range(len(bucket) - 1, 0, -1):
        for n in bucket[i]:
            res.append(n)
            if len(res) == k:
                return res

print(findTopK([1,1,1,2,2,3],2))