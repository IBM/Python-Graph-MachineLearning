def permute(self, nums):
    resultArr = []
    self.backtrack(nums,[],resultArr)
    #print(resultArr)
    return resultArr
    
def backtrack(self,nums,result,resultArr):
    #print(nums)
    if len(nums) == 0:
        resultArr.append(result)
        return
    else:
        for i in range(0,len(nums)):
            self.backtrack(nums[:i]+nums[i+1:],result+ [nums[i]],resultArr)

"""
Steps:--
if length of number becomes 0 then append result
else run for loop with backtrack where we  we pass all number except current and append to result

"""