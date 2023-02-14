class Solution:
    def maxProfit(self, prices) -> int:
        res = 0

        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res

"""
Steps:-
if price r is less than l, reset l to r
calculate max value diff and store it in result

"""