import sys

N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
maxNum = arr[0]
if maxNum > 1:
    print(1)
    exit()
for i in range(1, len(arr)):
    if arr[i] > maxNum + 1:
        break
    maxNum += arr[i]
print(maxNum + 1)