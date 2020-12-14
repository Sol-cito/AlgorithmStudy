import sys
from _collections import deque

# 해당 노드가 가장자리 노드인지 검증하는 함수. 가장자리가 아니면 큐에 넣을필요 없다. - 사방에 하나라도 0이 있으면 가장자리 노드임.
def checkIfEdge(x, y, arr):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for dir in directions:
        nx, ny = x + dir[0], y + dir[1]
        if 0 <= nx < len(arr) and 0 <= ny < len(arr) and arr[nx][ny] == 0:
            return True
    return False

#  가장자리 노드들을 담은 queue를 bfs로 한 번 더 탐색하면서 간척사업을 진행함.
def bfs2(que, arr):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visit = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
    res, endFlag = len(arr) * len(arr), 0
    while que:
        pop = que.pop()
        for dir in directions:
            nx, ny = pop[0] + dir[0], pop[1] + dir[1]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr):
                if arr[nx][ny] == 0 and endFlag == 0:
                    que.appendleft([nx, ny, pop[2], pop[3] + 1])
                    arr[nx][ny] = pop[2]
                    visit[nx][ny] = pop[3] + 1
                elif arr[nx][ny] != 0 and arr[nx][ny] != pop[2]:
                    # 간척사업이 만나는 경우 endFlag를 1로 만든다. 다리를 놓을 수 있는 지점이 발견되면 더이상 que에 append하지 않고
                    # que에 남아있는 것들만 검사하여 min값만 return
                    endFlag = 1
                    res = min(res, visit[nx][ny] + pop[3])
    return res

# 전체적으로 bfs로 한 바퀴를 돌면서 가장자리 노드에 flag 번호를 지정하여 que에 담음
def bfs1(x, y, arr, que, flag):
    arr[x][y] = flag
    tempQue = deque([[x, y, flag]])
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while tempQue:
        pop = tempQue.pop()
        if checkIfEdge(pop[0], pop[1], arr):
            que.appendleft([pop[0], pop[1], flag, 0])
        for dir in directions:
            nx, ny = pop[0] + dir[0], pop[1] + dir[1]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr) and arr[nx][ny] == 1:
                tempQue.appendleft([nx, ny])
                arr[nx][ny] = flag


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
que = deque([])
flag = 2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bfs1(i, j, arr, que, flag)
            flag += 1
print(bfs2(que, arr))
