array = [1,2,3]
n= len(array)
result = []
def permutation(arr, subset):
    if len(subset) == n:
        result.append(subset[::])
        return
    for i in range(len(arr)):
        subset.append(arr[i])
        permutation(arr[:i]+arr[i+1:], subset)
        subset.pop()
permutation(array, [])
print(result)

# c 4:2
array = [1,2,3,4]
k = 2
n = len(array)
ans2 = []

def combination(i, subset):
    if len(subset)== k:
        ans2.append(subset[::])
        return
    for j in range(i, n):
        subset.append(array[j])
        combination(j+1, subset)
        subset.pop()

combination(0, [])
print(ans2)