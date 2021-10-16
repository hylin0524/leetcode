array = [1,2,3,4]
n = len(array)

# method 1
ans1 = []
def backtracking(arr, temp):
    if len(temp) == n:
        ans1.append(temp)
        return
    for i in range(len(arr)):
        backtracking(arr[:i] + arr[i+1:], temp+[arr[i]])

backtracking(array, [])
print("method 1", ans1)

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
print("method 2", ans2)