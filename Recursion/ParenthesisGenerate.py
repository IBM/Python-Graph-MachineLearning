def generateParenthesis(self, n):
    def backtrack(p,left,right,ans):
        if left != 0:
            backtrack(p + '(',left -1,right,ans)
        if right > left:
            backtrack(p + ')',left,right-1,ans)
        if right == 0:
            ans.append(p)
        
        return ans
    ans = []
    return backtrack('',n,n,ans)

"""
Steps:-
set number of parenthesis to generate
if left is not 0, add open bracket to string , decrement left and backtrack
if right is not 0, add closing bracket to string , decrement right and backtrack
when right becomes 0, add combination to ans

"""