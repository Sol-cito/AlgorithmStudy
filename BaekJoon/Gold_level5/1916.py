import sys, heapq

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for i in range(M)]
S, E = map(int, sys.stdin.readline().strip().split(" "))
res = [[10000000000 for i in range(N)] for i in range(N)]
s, si = 10000000000, 0
for ele in arr:
    res[ele[0] - 1][ele[1] - 1] = min(res[ele[0] - 1][ele[1] - 1], ele[2])
    if ele[0] - 1 == S - 1 and ele[2] < s:
        s, si = ele[2], ele[1] - 1
visit = [0 for i in range(N)]
heap = [[s, si]]
for i in range(N):
    pop = heapq.heappop(heap)
    target, index = pop[0], pop[1]
    visit[index] = 1
    heap = []
    for j in range(N):
        res[S - 1][j] = min(res[S - 1][j], res[S - 1][index] + res[index][j])
        if visit[j] == 0: heapq.heappush(heap, [res[S - 1][j], j])
print(res[S - 1][E - 1])
