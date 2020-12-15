import sys

N, M = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))
arr1, arr2 = [], []
for i in range(len(arr)):
    arr1.append(abs(arr[i])) if arr[i] < 0 else arr2.append(arr[i])
arr1.sort()
arr2.sort()
res, p1, p2, cnt = 0, len(arr1) - 1, len(arr2) - 1, 0
while p1 >= 0 or p2 >= 0:
    a = arr1[p1] if p1 >= 0 else 0
    b = arr2[p2] if p2 >= 0 else 0
    if a > b:
        res = res + a if cnt == 0 else res + 2 * a
        p1 -= M
    else:
        res = res + b if cnt == 0 else res + 2 * b
        p2 -= M
    cnt += 1
print(res)
