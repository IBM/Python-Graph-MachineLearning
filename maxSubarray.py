class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSum = max(maxSum, currSum)
        return maxSum

"""
Steps:-
if currentsum negative then reset to 0
add value to currentSum
check if greater than max value and update

"""