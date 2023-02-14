class Solution:
    def trap(self, height) -> int:
        waterLevel = []
        left = 0
        for h in height:
            left = max(left, h) 
            waterLevel += [left] # over-fill it to left max height
            #print(waterLevel)
        right = 0
        for i, h in reversed(list(enumerate(height))):
            right = max(right, h)
            waterLevel[i] = min(waterLevel[i], right) - h # drain to the right height
        return sum(waterLevel)

"""
Steps:-
iterate left to right and set left max value and add to array.
iterate right to left and get min(max of right or max of left) - current height


"""