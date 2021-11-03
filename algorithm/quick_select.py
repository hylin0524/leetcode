# quick selct 
def partition(arr, l, r):
    pivot = arr[r]
    for i in range(l,r):
        # print(f"the left: {i} {arr[i]}, the right: {j} {arr[j]}")
        if arr[i] <= pivot: # swap condition
            arr[i], arr[l] = arr[l], arr[i]
            l += 1
    arr[l], arr[r] = arr[r], arr[l]
    return l


def quickselect(arr,l,r,k):
    while l <= r:
        pivot = partition(arr, l, r) # nums, 0, n-1

        if pivot == k-1:
            return arr[pivot]
        elif pivot > k-1: 
            r = pivot -1
        else:
            l = pivot +1
    
    return -1

nums = [3,6,2,1,4,5] 
# nums = [100,2,3,88,45,23]
n = len(nums)
k = 2 # smallest; largest = n-k+1

ans = quickselect(nums, 0, n-1, n-k+1)
print(ans)