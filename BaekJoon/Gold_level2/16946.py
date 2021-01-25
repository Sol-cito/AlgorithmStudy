import sys
from collections import deque


def bfs(i, j, arr, valArr, visit, targetVisit, flag):
    que = deque([[i, j]])
    visit[i][j] = 1
    targetOfSwtich, targetVal = [], 0
    while que:
        pop = que.pop()
        targetVal += 1
        for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1]:
            nx, ny = pop[0] + dx, pop[1] + dy
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] != 1 and visit[nx][ny] == 0:
                que.append([nx, ny])
                visit[nx][ny] = 1
            elif 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] == 1 and targetVisit[nx][ny] != flag:
                targetOfSwtich.append([nx, ny])
                targetVisit[nx][ny] = flag
    for ele in targetOfSwtich:
        valArr[ele[0]][ele[1]] += targetVal


N, M = map(int, sys.stdin.readline().split(" "))
arr = [[int(ele) for ele in sys.stdin.readline().rstrip()] for _ in range(N)]
valArr = [[0] * M for _ in range(N)]
visit = [[0] * M for _ in range(N)]
targetVisit = [[0] * M for _ in range(N)]
flag = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visit[i][j] == 0:
            bfs(i, j, arr, valArr, visit, targetVisit, flag)
            flag += 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(0, end="")
        else:
            print((valArr[i][j] + 1) % 10, end="")
    print()
