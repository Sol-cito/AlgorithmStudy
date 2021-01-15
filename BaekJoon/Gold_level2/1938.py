import sys
from collections import deque


def check(arr, visit, numMap, x1, x2, y1, y2, z1, z2):
    if 0 <= x1 < len(arr) and 0 <= x2 < len(arr) and 0 <= y1 < len(arr) and 0 <= y2 < len(arr) and 0 <= z1 < len(
            arr) and 0 <= z2 < len(arr) \
            and (arr[x1][x2] in ('0', 'E', 'B')) and (arr[y1][y2] in ('0', 'E', 'B')) and (
            arr[z1][z2] in ('0', 'E', 'B')) \
            and visit[numMap[x1][x2]][numMap[z1][z2]] == 0:
        return True
    return False


# 통나무가 세로일 때
def ninetyCheck1(arr, x1, x2, y1, y2, z1, z2):
    for d in [-1, 1]:
        if 0 <= x2 + d < len(arr) and 0 <= y2 + d < len(arr) and 0 <= z2 + d < len(arr) \
                and arr[x1][x2 + d] in ('0', 'E', 'B') and arr[y1][y2 + d] in ('0', 'E', 'B') \
                and arr[z1][z2 + d] in ('0', 'E', 'B'):
            continue
        else:
            return False
    return True


# 통나무가 가로일 때
def ninetyCheck2(arr, x1, x2, y1, y2, z1, z2):
    for d in [-1, 1]:
        if 0 <= x1 + d < len(arr) and 0 <= y1 + d < len(arr) and 0 <= z1 + d < len(arr) and (
                arr[x1 + d][x2] in ('0', 'E', 'B')) and (arr[y1 + d][y2] in ('0', 'E', 'B')) and (
                arr[z1 + d][z2] in ('0', 'E', 'B')):
            continue
        else:
            return False
    return True


N = int(sys.stdin.readline())
arr = [[i for i in sys.stdin.readline().rstrip()] for _ in range(N)]
numMap = [[i for i in range(N)] for _ in range(N)]
cnt = 0
B = []
for i in range(N):
    for j in range(N):
        numMap[i][j] = cnt
        cnt += 1
        if arr[i][j] == 'B': B.append([i, j])
B.append(0)
que = deque([B])
visit = [[0 for _ in range(N * N)] for _ in range(N * N)]
visit[numMap[B[0][0]][B[0][1]]][numMap[B[2][0]][B[2][1]]] = 1
visit[numMap[B[2][0]][B[2][1]]][numMap[B[0][0]][B[0][1]]] = 1
while que:
    pop = que.pop()
    if arr[pop[0][0]][pop[0][1]] == arr[pop[1][0]][pop[1][1]] == arr[pop[2][0]][pop[2][1]] == 'E':
        print(pop[3])
        exit()
    for dx, dy in [1, 0], [0, 1], [-1, 0], [0, -1]:
        if check(arr, visit, numMap, pop[0][0] + dx, pop[0][1] + dy, pop[1][0] + dx, pop[1][1] + dy, pop[2][0] + dx,
                 pop[2][1] + dy):
            que.appendleft(
                [[pop[0][0] + dx, pop[0][1] + dy], [pop[1][0] + dx, pop[1][1] + dy], [pop[2][0] + dx, pop[2][1] + dy],
                 pop[3] + 1])
            visit[numMap[pop[0][0] + dx][pop[0][1] + dy]][numMap[pop[2][0] + dx][pop[2][1] + dy]] = 1
            visit[numMap[pop[2][0] + dx][pop[2][1] + dy]][numMap[pop[0][0] + dx][pop[0][1] + dy]] = 1
    #  통나무가 세로모양일 때
    if pop[0][1] == pop[2][1] and check(arr, visit, numMap, pop[0][0] + 1, pop[0][1] - 1, pop[1][0],
                                        pop[1][1], pop[2][0] - 1, pop[2][1] + 1) \
            and ninetyCheck1(arr, pop[0][0], pop[0][1], pop[1][0], pop[1][1], pop[2][0], pop[2][1]):
        que.appendleft(
            [[pop[0][0] + 1, pop[0][1] - 1], [pop[1][0], pop[1][1]], [pop[2][0] - 1, pop[2][1] + 1],
             pop[3] + 1])
        visit[numMap[pop[0][0] + 1][pop[0][1] - 1]][numMap[pop[2][0] - 1][pop[2][1] + 1]] = 1
        visit[numMap[pop[2][0] - 1][pop[2][1] + 1]][numMap[pop[0][0] + 1][pop[0][1] - 1]] = 1
    #  통나무가 가로모양일 때
    if pop[0][0] == pop[2][0] and check(arr, visit, numMap, pop[0][0] - 1, pop[0][1] + 1, pop[1][0],
                                        pop[1][1], pop[2][0] + 1, pop[2][1] - 1) \
            and ninetyCheck2(arr, pop[0][0], pop[0][1], pop[1][0], pop[1][1], pop[2][0], pop[2][1]):
        que.appendleft(
            [[pop[0][0] - 1, pop[0][1] + 1], [pop[1][0], pop[1][1]], [pop[2][0] + 1, pop[2][1] - 1],
             pop[3] + 1])
        visit[numMap[pop[0][0] - 1][pop[0][1] + 1]][numMap[pop[2][0] + 1][pop[2][1] - 1]] = 1
        visit[numMap[pop[2][0] + 1][pop[2][1] - 1]][numMap[pop[0][0] - 1][pop[0][1] + 1]] = 1
print(0)
