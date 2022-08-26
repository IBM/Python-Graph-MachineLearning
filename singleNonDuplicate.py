class Solution:
    def singleNonDuplicate(self, nums) -> int:
        
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            left = max(0,mid-1)
            right = min(len(nums)-1,mid+1)
            if mid != 0 and nums[left] == nums[mid]:
                if mid%2 == 1:
                    lo = mid+1
                else:
                    hi = mid-2
            elif mid != len(nums)-1 and nums[right] == nums[mid]:
                if (mid-1)%2 == 1:
                    lo = mid+2
                else:
                    hi = mid-1
            else:
                return nums[mid]
        return nums[lo]

s = Solution()
print(s.singleNonDuplicate([1,1,2,2,3,3,4,8,8]))