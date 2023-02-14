import heapq 
small = []
large = []

heapq.heappush(small,2)
heapq.heappush(small,-2)
heapq.heappush(small,-4)

print(heapq.heappop(small))