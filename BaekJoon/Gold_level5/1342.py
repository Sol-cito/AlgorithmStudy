import sys
from collections import Counter


def recurse(dic, keyList, leng, curLeng, p, res):
    if curLeng == leng:
        return res + 1

    for i in range(len(keyList)):
        if i == p: continue
        if dic.get(keyList[i]) != 0:
            dic[keyList[i]] -= 1
            res = recurse(dic, keyList, leng, curLeng + 1, i, res)
            dic[keyList[i]] += 1
    return res


S = sys.stdin.readline().rstrip()
dic = Counter(S)
keyList = list(dic.keys())
print(recurse(dic, keyList, len(S), 0, -1, 0))
