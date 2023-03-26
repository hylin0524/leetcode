"""
解法: 
1. build最後一位補0, packs第一位補build[0]
2. 紀錄lmax的數字, lmax=前一輪b,p取較大
3. b因為不會idle所以他自己+自己
4. p會受到自己和b值影響，所以要加上bp最大

"""
# build = [4,2,5,0]
# packs = [4,2,3,2] 
# build = [2,4,3,5,0]
# packs = [2,5,2,3,6] 
# build = [3,2,1,0]
# packs = [3,1,1,2]
# build = [1,1,2,0]
# packs = [1,3,2,1]
build = [13,12,11,0]
packs = [13,6,12,3]

ans = []
b,p,l = build[0],build[0],len(build)
idle = build[0]

for i in range(1,l):
    lmax = max(b,p)
    if b-p > 0:
        idle += (b-p)
    b += build[i]
    p = packs[i] + lmax
    ans.append(p)

ans.append(idle)
print(ans)