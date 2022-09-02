class Solution:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums) - 1
        boundary_index = -1

        while left <= right:
            mid = (left + right) // 2
            # if <= last element, then belongs to lower half
            if nums[mid] <= nums[-1]:
                boundary_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return nums[boundary_index]

"""
Steps:-
set left and right index
run a while loop till left less than right
get midpoint and check if its less than last value r
if yes then set boundry index as mid and decrement right to mid - 1
else mid + 1


"""


class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
"""
Steps:-
set left and right index
run a while loop till left less than right
get midpoint and check if target == mid

left sorted:-
if left less than mid and target is not in that range, set l to mid +1
if left less than mid and target is  in that range, set r to mid - 1

right sorted
if left is greater than mid and target not in range mid and r, then set r to mid - 1
if left is greater than mid and target not  range mid and r, then set l to mid + 1
"""