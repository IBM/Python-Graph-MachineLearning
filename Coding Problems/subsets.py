
def subsets(nums) :
    result = []
    combination = []
      
       
    def backtrack2(nums,combination,result):
        if len(nums) == 0:
            return
        else:
            if nums not in result:
                
                result.append(nums)
            for i in range(0,len(nums)):
                combination.append(nums)
                backtrack2(nums[:i] + nums[i+1:],combination,result)

        print(result)            
    backtrack2(nums,combination,result)
                
    
                  
class Solution:
    def subsets(self, nums):
        res = []
        def dfs(i, comb):
            if i == len(nums):
                res.append(comb)
                return
            dfs(i+1, comb + [nums[i]])
            dfs(i+1, comb)
            return
        dfs(0, [])
        print(res)
        return res
s = Solution()  
s.subsets([1,2,3])

# 1       
# [2,3] 

    #     [123]
    #   [12] [23]
    # [1][2] [2][3]