import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
dic = {}
for i in range(N):
    s = sys.stdin.readline().rstrip()
    if s in dic:
        dic[s] = dic.get(s) + 1
    else:
        dic[s] = 1
K = int(sys.stdin.readline().rstrip())
res = 0
for ele in dic:
    z = ele.count("0")
    if K >= z and (K - z) % 2 == 0:
        res = max(res, dic.get(ele))
print(res)
