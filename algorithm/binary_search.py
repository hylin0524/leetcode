# test case
array = [4,2,6,9,10,27,6,12]
array.sort()
target = 4

def binary_search():
    l, r = 0, len(array)-1
    while l <= r:
        mid = l + (r-l)//2
        if array[mid] == target:
            return mid
        if array[mid] > target:
            r = mid
        else:
            l = mid+1
    return -1

ans = binary_search()
print(ans)