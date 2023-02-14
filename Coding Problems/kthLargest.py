from collections import heapq

class Solution:
    def findKthLargest(self, nums) -> int:
        # count = collections.defaultdict(int)
        # for n in nums:
        #     count[n] += 1
        
        maxHeap = []
        for i, n in enumerate(nums):
            heapq.heappush(maxHeap, (-n, i))
        
        for _ in range(k-1):
            heapq.heappop(maxHeap)
        
        return maxHeap[0][0] * -1