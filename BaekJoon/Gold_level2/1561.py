import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
if N <= M:
    print(N)
    exit()
left, right = 1, 60000000001
sum = 0
while left <= right:
    mid = int((left + right) // 2)
    sum = M
    for ele in arr:
        sum += mid // ele
    if sum < N:
        left = mid + 1
    else:
        right = mid - 1
sum = M
for ele in arr:
    sum += min(left, right) // ele
for i in range(len(arr)):
    if (min(left, right) + 1) % arr[i] == 0:
        sum += 1
    if sum == N:
        print(i + 1)
        exit()
