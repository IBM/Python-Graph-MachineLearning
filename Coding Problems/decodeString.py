class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                subStr = ''
                while stack[-1] != '[':
                    subStr = stack.pop() + subStr
                stack.pop()
                numStr = ''
                while stack and stack[-1].isdigit():
                    numStr = stack.pop() + numStr
                
                stack.append(int(numStr) * subStr)
        return ''.join(stack)