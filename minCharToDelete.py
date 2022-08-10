class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a = collections.Counter(s)
        b = collections.Counter(t)
		# Uncomment following lines Just to check what's actually happening.
        # print(a)
        # print(b)
        # print(a-b, sum((a-b).values()))
        # print(b-a, sum((b-a).values()))
        # print(sum((a-b).values()), sum((b-a).values()))
       
        return sum((a-b).values())