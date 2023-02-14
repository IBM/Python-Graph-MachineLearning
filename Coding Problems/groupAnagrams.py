import collections
class Solution:
    def groupAnagrams(self, strs) :
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 90
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
            print(tuple(count))
        return ans.values()
s = Solution()
print(s.groupAnagrams(["Yat","tea","tan","ate","nat","bat"]))
#print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


for i in range(10,0,-1):
    print(i)