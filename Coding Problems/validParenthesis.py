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

"""
Steps:
create dictionary with closiung brackets as key and opening brackets as value
if last value in stack is equal to dictionary value
then pop
else add to stack

"""