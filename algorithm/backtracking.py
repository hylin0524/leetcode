'''
backtracking pattern
1. condition of recursive terminate 
2. backtrack logic, include or not?
'''

array = [1,2,3,4]
n = len(array)

# method 1
ans1 = []
def backtracking(arr, subset):
    if len(subset) == n:
        ans1.append(subset[::])
        return
    for i in range(len(arr)):
        subset.append(arr[i])
        backtracking(arr[:i] + arr[i+1:], subset)
        subset.pop()

backtracking(array, [])
print("\nmethod 1\n", ans1)

# method 2
ans2 = []
visited = set()

def backtracking_visit(arr, visited, temp):
    if len(temp) == n:
        ans2.append(temp)
    for i in range(len(arr)):
        if i not in visited:
            visited.add(i)
            backtracking_visit(arr, visited, temp+[arr[i]])
            visited.remove(i)

backtracking_visit(array, visited, [])
print("\nmethod 2\n", ans2)

# subset
nums = [1,2,3]
n = len(nums)
subset_ans = []

def subsets(start, subset):
    if start == n:
        subset_ans.append(subset[::])
        return
    subset.append(nums[start]) # [1]
    subsets(start+1, subset)
    subset.pop() # []
    subsets(start+1, subset)

subsets(0, [])
print("\nsubset uniqle\n", subset_ans)