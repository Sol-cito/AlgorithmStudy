import sys

N, M = map(int, sys.stdin.readline().split(" "))
trees = list(map(int, sys.stdin.readline().split(" ")))

l, r = 0, max(trees)
res = 0
while l <= r:
    mid = int((l + r) / 2)
    sum = 0
    for tree in trees:
        if tree - mid > 0: sum += tree - mid
    if sum >= M:
        res = max(res, mid)
        l = mid + 1
    else:
        r = mid - 1
print(res)
