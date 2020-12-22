import sys
from functools import reduce


# 최소 한 개의 모음, 최소 두 개의 자음으로 구성
# 모음이 하나도 없거나, 자음이 하나 이하거나

def moDFS(wList, mo, word, limit, idx):
    if len(word) > 0:
        wList.append(word)
    if len(word) < limit:
        for i in range(idx, len(mo)):
            moDFS(wList, mo, word + mo[i], limit, i + 1)


def jaDFS(res, ja, word, limit, idx):
    if len(word) == limit:
        res.append(reduce(lambda x, y: x + y, (sorted(word))))
        return
    for i in range(idx, len(ja)):
        jaDFS(res, ja, word + ja[i], limit, i + 1)


L, C = map(int, sys.stdin.readline().split(" "))
arr = sys.stdin.readline().rstrip().split(" ")
ja = sorted([ele for ele in arr if ele not in ['a', 'e', 'i', 'o', 'u']])
mo = sorted([ele for ele in arr if ele in ['a', 'e', 'i', 'o', 'u']])
wList, res = [], []
moDFS(wList, mo, "", L - 2, 0)
for word in wList:
    jaDFS(res, ja, word, L, 0)
res.sort()
for ele in res:
    print(ele)
