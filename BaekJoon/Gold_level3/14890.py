import sys


def construction2(row, builtRow, start, L):
    cnt = 0
    for i in range(start, max(-1, start - L), -1):
        if row[i] == row[start] and builtRow[i] == 0:
            cnt += 1
    if cnt == L:
        for i in range(start, max(-1, start - L), -1):
            builtRow[i] = -1
        return True
    return False


def construction1(row, builtRow, start, L):
    cnt = 0
    for i in range(start, min(len(row), start + L)):
        if row[i] == row[start] and builtRow[i] == 0:
            cnt += 1
    if cnt == L:
        for i in range(start, min(len(row), start + L)):
            builtRow[i] = -1
        return True
    return False


def search(row, builtRow, L):
    for i in range(len(row) - 1):
        # 높이 차이가 1 이상이면 false 리턴
        if abs(row[i] - row[i + 1]) > 1: return False
        #  왼쪽이 더 높을 때
        if row[i] == row[i + 1] + 1:
            if not construction1(row, builtRow, i + 1, L):
                return False
        # 오른쪽이 더 높을 때
        elif row[i] + 1 == row[i + 1]:
            if not construction2(row, builtRow, i, L):
                return False
    return True


N, L = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
res = 0
for i in range(N):
    built = [[0 for _ in range(N)] for _ in range(N)]
    if search(arr[i], built[i], L): res += 1
for i in range(N):
    built = [[0 for _ in range(N)] for _ in range(N)]
    if search([j[i] for j in arr], [j[i] for j in built], L): res += 1
print(res)