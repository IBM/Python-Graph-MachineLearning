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