
phone = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
result = []
combination = ""
def letterCombinations(digits: str) :
    if len(digits) == 0:
        return []
    phoneDic = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
    result = []
    combination = ""
    res = backtrack(digits,phoneDic,combination,result)
    return result
    
def backtrack(digits,phoneDic,combination,result):
    if len(digits) == 0:
        result.append(combination)
        return result
    else:
        for char in phoneDic[digits[0]]:
            backtrack(digits[1:],phoneDic,combination +char,result)
            
        
    
letterCombinations("23")

"""
Steps:-
create dictionary for each number and their letter
do backtrack
    check for each digit and its char nodes and add it to combination
    increment inoput digit and recursively call function

"""