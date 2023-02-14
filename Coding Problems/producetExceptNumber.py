class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        
        prefix = 1
        #get range previous multiplied value in arr
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
    
sol = Solution()
print(sol.productExceptSelf([2,4,6,8]))

#[2,4,6,8]
# 1 2 8 48

"""
Steps:-

set array of 1 to size of nums
prefix = 1
update value of res by prefix
multiply prefix by number

postfix = 1
go from right to left
multiply value by postfix
multiply postfix by number
"""