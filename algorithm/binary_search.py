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


def binary_search_duplicate(array, target):
    # if target are dupliated, then we return left most index.
    l, r = 0, len(array) - 1
    while l < r:
        m = (l+r)//2
        if array[m] < target:
            l = m + 1
        else:
            r = m
    return l

binary_search_duplicate([5,6,8,8,8,9,9,11], 10) # idx = 7
binary_search_duplicate([5,6,8,8,8,9,9,11], 9) # idx = 5
