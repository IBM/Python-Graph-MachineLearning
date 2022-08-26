class Solution:
    def maxArea(self, height) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l<r:
            currArea = abs(r-l) * min(height[l], height[r])
            res = max(currArea, res)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res