import sys
from _collections import deque


def bfs(dirt, arr, dist):
    que = deque([dirt])
    visit = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    visit[dirt[0]][dirt[1]] = 1
    while que:
        pop = que.pop()
        if arr[pop[0]][pop[1]] not in ('x', '.'):
            dist[arr[dirt[0]][dirt[1]]][arr[pop[0]][pop[1]]] = pop[2]
        for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1]:
            if 0 <= pop[0] + dx < len(arr) and 0 <= pop[1] + dy < len(arr[0]) and arr[pop[0] + dx][pop[1] + dy] != 'x' \
                    and visit[pop[0] + dx][pop[1] + dy] == 0:
                visit[pop[0] + dx][pop[1] + dy] = 1
                que.appendleft([pop[0] + dx, pop[1] + dy, pop[2] + 1])


def recursion(startNum, total, res, dist, visit, returnVal):
    if total == len(dist) - 1:
        return res
    for dirtNum in range(len(dist[startNum])):
        if visit[dirtNum] == 0:
            visit[dirtNum] = 1
            returnVal = min(returnVal,
                            recursion(dirtNum, total + 1, res + dist[startNum][dirtNum], dist, visit, returnVal))
            visit[dirtNum] = 0
    return returnVal


while 1:
    col, row = map(int, sys.stdin.readline().rstrip().split(" "))
    if col == row == 0:
        exit()
    arr = [[i for i in sys.stdin.readline().rstrip()] for _ in range(row)]
    dirtLocation, dirtCnt = [], 1
    for i in range(row):
        for j in range(col):
            if arr[i][j] == '*':
                dirtLocation.append([i, j, 0])
                arr[i][j] = dirtCnt
                dirtCnt += 1
            if arr[i][j] == 'o':
                dirtLocation.append([i, j, 0])
                arr[i][j] = 0
    dist = [[0 for _ in range(dirtCnt)] for _ in range(dirtCnt)]
    for dirt in dirtLocation:
        bfs(dirt, arr, dist)
    visit = [0] * len(dist)
    visit[0] = 1
    zeroCnt = 0
    for i in range(1, len(dist[0])):
        if dist[0][i] == 0:
            zeroCnt += 1
            break
    if zeroCnt == 0:
        print(recursion(0, 0, 0, dist, visit, len(dist) * col * row + 1))
    else:
        print(-1)
