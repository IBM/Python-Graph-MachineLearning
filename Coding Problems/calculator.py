class Solution:  #772. Basic Calculator III
    def calculate(self, s: str) -> int:
        if not s:
             return -1
        squence = list(s)
        return self.cal(squence) 
    
    def cal(self, s):
        stack = []
        num = 0
        sign = '+'              #previous sign
        while len(s) > 0:        #while condition
            char = s.pop(0)      #!!!popleft
            if char.isdigit():
                num = 10 * num + int(char)  # 10*num +int
                
            if char == '(':      #recursive when meet (
                num = self.cal(s)
            # change condition or stop    
            if char in '+-*/)' or len(s) == 0:
                if sign =='+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                # high privilage than + -
                if sign == '*':
                    stack[-1] = num * stack[-1]
                if sign == '/':
                    stack[-1] = int(stack[-1] / float(num))  # divide close to 0 
                num = 0
                sign = char
                
            if char == ')': #recursive stop meet )
                break
                
        return sum(stack)