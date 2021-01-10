import sys

K, N = map(int, sys.stdin.readline().split(" "))
arr = [int(sys.stdin.readline()) for i in range(K)]
l, r, res = 1, max(arr), 0
while l <= r:
    mid = (l + r) // 2
    total = 0
    for ele in arr:
        total += ele // mid
    if total >= N:
        res = max(res, mid)
        l = mid + 1
    else:
        r = mid - 1
print(res)
