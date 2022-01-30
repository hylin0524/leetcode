import heapq

from numpy import arange
''' 
Scenario:
    1. used to sort
    2. find k largest/smallest in array
'''

# heapq is min-heap in Python Libray
num_for_min_heap = [100,9,3,59,12]
origin = num_for_min_heap[::]
heapq.heapify(num_for_min_heap)
sort_asc = []

while num_for_min_heap:
    a = heapq.heappop(num_for_min_heap)
    sort_asc.append(a)

print(f"origin {origin}, ascending {sort_asc}")
'''
output:
origin [100, 9, 3, 59, 12], descending [3, 9, 12, 59, 100]
'''

# Implement in max-heap
num_for_max_heap = [23,68,-4,3,-1]
heap = []
heapq.heapify(heap)

for n in num_for_max_heap:
    heapq.heappush(heap, -n)

sort_desc = []
while heap:
    a = heapq.heappop(heap)
    sort_desc.append(-a)
print(f"origin {num_for_max_heap}, descending {sort_desc}")
'''
output:
origin [23, 68, -4, 3, -1], descending [68, 23, 3, -1, -4]
'''

# store the index in heapq
array = [100,9,3,59,12]
result = []
heapq.heapify(result)

for i,v in enumerate(array):
    heapq.heappush(result, (v,i))

while result:
    v, i = heapq.heappop(result)
    print(f"value: {v} | key: {i}")

'''
output:
value: 3 | key: 2
value: 9 | key: 1
value: 12 | key: 4
value: 59 | key: 3
value: 100 | key: 0
'''

# find k largest element
def k_largest(array, k):
    heapq.heapify(array)

    # k = len(array) - k + 1
    print(k)
    while array:
        if len(array) == k:
            return heapq.heappop(array)
        heapq.heappop(array)
        
ans = k_largest([100,9,3,59,12], 2)
print(ans) 
'''
output: 59
'''
