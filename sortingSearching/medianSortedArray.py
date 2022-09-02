def findMedianSortedArrays(self, nums1, nums2) -> float:
    
    nums = nums1+nums2
    nums.sort()
    n = len(nums)
    
    if n%2==0:
        mid =int(n/2) 
        median = (nums[mid]+nums[mid-1])/2
        return median
    else:
        mid = (n-1)/2
        median = int(mid)
        return nums[median]