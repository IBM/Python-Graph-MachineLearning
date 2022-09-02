from collections import deque,defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        self.graph = defaultdict(list)
        self.outdegree = defaultdict(int)
        self.createGraph(prerequisites)
        return self.getOrder(numCourses)
        
        
        
    def createGraph(self,prerequisites):
        #create graph with indepandent values as key and dependant values as values.
        #increase outer degree for dependant values.
        for depandent,indepandent in prerequisites:
            self.graph[indepandent].append(depandent)
            self.outdegree[depandent] +=1
    
    def getOrder(self,numCourses):
        queue = deque()
        ordering = []
        #if outer degree = 0 then no dependancy, add to queue.
        for i in range(numCourses):
            if self.outdegree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            ordering.append(course)
            #decrement outer degree and if 0 then add to queue as there is no more dependancy.
            for i in self.graph[course]:
                self.outdegree[i] -= 1
                if self.outdegree[i] == 0:
                    queue.append(i)

        if len(ordering)==numCourses:
            return ordering
        else:
            return []

            
        
s = Solution()
print(s.findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))

"""
#steps:-
create dic for values and outer degree

find all courses with outer degree 0 ie no dependancies and ad to queue
pop values from queue and add to ans array.
check for all the courses dependant on this one and decrement their outer degree
if outer degree 0 add to queue

"""