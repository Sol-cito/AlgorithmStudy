import sys
from collections import deque


def bfs(arr, ji_que, fire_que):
    while ji_que:
        nJiQue = deque([])
        while ji_que:
            pop = ji_que.pop()
            if arr[pop[0]][pop[1]] != 'J': continue
            for dx, dy in [0, 1], [1, 0], [-1, 0], [0, -1]:
                nx, ny = pop[0] + dx, pop[1] + dy
                if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and arr[nx][ny] in ['.', 0]:
                    if arr[nx][ny] == 0:
                        return pop[2] + 1
                    arr[nx][ny] = 'J'
                    nJiQue.append([nx, ny, pop[2] + 1])
        ji_que = nJiQue
        nFire_que = deque([])
        while fire_que:
            firePop = fire_que.pop()
            for dx, dy in [0, 1], [1, 0], [-1, 0], [0, -1]:
                nx, ny = firePop[0] + dx, firePop[1] + dy
                if 1 <= nx < len(arr) - 1 and 1 <= ny < len(arr[0]) - 1 and arr[nx][ny] not in ['F', '#']:
                    arr[nx][ny] = 'F'
                    nFire_que.append([nx, ny])
        fire_que = nFire_que
    return -1


R, C = map(int, sys.stdin.readline().split(" "))
arr = [[0 for _ in range(C + 2)] for _ in range(R + 2)]
ji_que = deque([])
fire_que = deque([])
for i in range(1, R + 1):
    input = sys.stdin.readline().rstrip()
    for j in range(1, C + 1):
        arr[i][j] = input[j - 1]
        if arr[i][j] == 'J': ji_que.append([i, j, 0])
        if arr[i][j] == 'F': fire_que.append([i, j])
res = bfs(arr, ji_que, fire_que)
if res < 0:
    print("IMPOSSIBLE")
else:
    print(res)