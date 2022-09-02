
class Solution:
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        for i,v in enumerate(values):
            res += (num//v) * numerals[i]
            num %= v
        
        return res
s = Solution()
s.intToRoman(3)