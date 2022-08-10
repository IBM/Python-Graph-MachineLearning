class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], res)
        return res

    def backtrack(self, candidates, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(candidates)):
            self.backtrack(candidates, target-candidates[i], i, path+[candidates[i]], res)