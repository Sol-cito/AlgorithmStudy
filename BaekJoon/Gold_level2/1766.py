import sys, heapq

N, M = map(int, sys.stdin.readline().split(" "))
dic = dict(zip([i for i in range(1, N + 1)], [[] for _ in range(N)]))
links = [0 for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    dic.get(a).append(b)
    links[b - 1] += 1
res, heap = [], []
for i in range(1, N + 1):
    if links[i - 1] == 0:
        heapq.heappush(heap, i)
        links[i - 1] = -1
while heap:
    pop = heapq.heappop(heap)
    for linkedNode in dic.get(pop):
        links[linkedNode - 1] -= 1
        if links[linkedNode - 1] == 0:
            heapq.heappush(heap, linkedNode)
            links[linkedNode - 1] = -1
    res.append(pop)
for ele in res: print(ele, end=" ")