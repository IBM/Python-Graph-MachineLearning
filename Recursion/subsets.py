def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    def dfs(i, comb):
        if i == len(nums):
            res.append(comb[:])
            return
        dfs(i+1, comb + [nums[i]])
        dfs(i+1, comb)
        return
    dfs(0, [])
    return res
    
"""
Steps:-
if we reach end of nums length, return combination
else dfs where we increment i and add num, where we dont add num

"""