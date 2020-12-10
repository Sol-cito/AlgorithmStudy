import sys


def search(arr, row):
    cnt = 0
    for i in range(row + 1, len(arr)):
        flag = True
        for j in range(len(arr[0])):
            if arr[i][j] != arr[row][j]:
                flag = False
                break
        if flag: cnt += 1
    return cnt


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
arr = [[int(ele) for ele in sys.stdin.readline().rstrip()] for i in range(N)]
K = int(sys.stdin.readline())
res = 0
for row in range(N):
    cnt = 0
    rowCnt = 1
    for col in range(M):
        if arr[row][col] == 0: cnt += 1
    if cnt <= K and (K - cnt) % 2 == 0:
        rowCnt += search(arr, row)
        res = max(res, rowCnt)
print(res)
