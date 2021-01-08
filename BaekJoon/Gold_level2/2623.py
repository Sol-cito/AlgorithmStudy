import sys
from _collections import deque

N, M = map(int, sys.stdin.readline().split(" "))
dic = {}
arr = [0] * N
que = deque([])
for _ in range(M):
    l = list(map(int, sys.stdin.readline().split(" ")))
    for j in range(1, len(l) - 1):
        if l[j] not in dic:
            dic[l[j]] = [l[j + 1]]
        else:
            dic.get(l[j]).append(l[j + 1])
        arr[l[j + 1] - 1] += 1
for i in range(len(arr)):
    if arr[i] == 0: que.appendleft(i + 1)
res = []
while que:
    pop = que.pop()
    res.append(pop)
    if dic.get(pop):
        for link in dic.get(pop):
            arr[link - 1] -= 1
            if arr[link - 1] == 0: que.appendleft(link)
if len(res) < N:
    print(0)
else:
    [print(ele) for ele in res]
