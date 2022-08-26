class Solution:
    def lengthOfLIS(self, nums) -> int:

        def binarySearch(arr,n):
            st=0
            ed=len(arr)-1
            while st<=ed:
                mid=(st+ed)//2
                if arr[mid]==n:
                    return mid
                elif arr[mid]>n:
                    ed=mid-1
                else:
                    st=mid+1
            return st
        
        
        ans=[]
        ans.append(nums[0])
        for i in range(1,len(nums)):
            if ans[-1]<nums[i]:
                ans.append(nums[i])
            else:
                idx=binarySearch(ans,nums[i])
                ans[idx]=nums[i]
        print(ans)
        return len(ans)

obj = Solution()
print(obj.lengthOfLIS([10,9,2,5,3,7,101,18]))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res