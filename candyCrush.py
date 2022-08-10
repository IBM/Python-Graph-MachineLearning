class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(v * num for v, num in stack)
    
s = Solution()
ans = s.removeDuplicates("deeedbbcccbdaa",3) 
print(ans)