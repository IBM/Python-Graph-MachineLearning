def merge(nums1, m, nums2, n):
    
        for i in range(len(nums1),-1,-1):
            print(i)
        nums1 = nums1[:m]
        i = j = 0
        while i < m:
            if nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j],nums1[i]
                
            elif nums1[i] <= nums2[j]:
                i += 1
        
        nums1 = nums1 + nums2
        return nums1
         
res = merge([1,2,3,0,0,0],3,[2,5,6],3)
print(res)

#[1,2,3,0,0,0]
#[2,5,6]

