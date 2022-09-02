def subarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    count = 0
    sums = 0
    d = dict()
    d[0] = 1
    
    for i in range(len(nums)):
        sums += nums[i]
        count += d.get(sums-k,0)
        d[sums] = d.get(sums,0) + 1
    
    return(count)

"""
Steps:-
add value to sum
check if sum-k value present in dic else return 0
add sums as value in dictionary
"""