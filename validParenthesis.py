class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for char in s:
            if stack and char in valid and stack[-1] == valid[char]:
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0