from collections import defaultdict
class Solution:
    
    def totalFruit(self, fruits) -> int:
        #[1,2,3,2,2] = > dic.keys() == 2,
#           l i
        dic = defaultdict(list)
        left = 0
        maxFruits = 0
        for i in range(len(fruits)):
            if fruits[i] not in dic:
                dic[fruits[i]] = i
            else:
                
                if len(dic.keys()) > 2:
                    maxFruits = max(maxFruits,i-1-left+1)
                    dic.pop(fruits[left])
                    
                    left = dic[fruits[i-1]]
                elif i == len(fruits)-1:
                    maxFruits = max(maxFruits,i-left+1)
                
        print(dic)   
        print("left",left)
        return maxFruits

#[3,3,3,1,2,1,1,2,3,3,4]
# l i

s = Solution()
s.totalFruit([1,2,3,2,2])


