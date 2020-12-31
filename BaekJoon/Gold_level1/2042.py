# prefix sum 배열과 dictionary를 이용하여 풀었으나 too slow
# 시간복잡도 : O(M * K) : M번 변경이 일어난 것을 K번 탐색함 -> Pypy로 통과
# 정석은 segment tree 를 이용하는 것이라 한다.

import sys


def cal(arr, hap, alter, fr, to):
    sum = hap[to - 1] - hap[fr - 2] if fr > 1 else hap[to - 1]
    for idx in alter.keys():
        if fr <= idx <= to:
            if arr[idx - 1] > alter.get(idx):
                sum -= arr[idx - 1] - alter.get(idx)
            elif arr[idx - 1] < alter.get(idx):
                sum += alter.get(idx) - arr[idx - 1]
    print(sum)


N, M, K = map(int, sys.stdin.readline().split(" "))
arr, hap = [], []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
    hap.append(arr[i]) if len(hap) == 0 else hap.append(hap[i - 1] + arr[i])
alter = {}
for i in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    if a == 1:
        alter[b] = c
    else:
        cal(arr, hap, alter, b, c)