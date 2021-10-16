
# basic: fibonacci
def fib(n):
    arr = [0, 1]
    for i in range(2,n):
        arr.append(arr[i-1] + arr[i-2])
    return arr

fib_ans = fib(8)
print(fib_ans)

# basic: Longest Common Subsequence
# careful columns and rows
def lcs(a, b):
    m, n = len(a), len(b) # 3, 5
    dp = [ [0]*(m+1) for i in range(n+1) ]

    for i in range(n): #
        for j in range(m): #
            if a[j] == b[i]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    return dp[-1][-1]

lcs_ans = lcs("ace", "abcde")
# lcs_ans = lcs("abc","def")
print(lcs_ans)
