import sys

N = int(sys.stdin.readline())
dic, l = {}, 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    dic.get(a).append(b) if a in dic else dic[a] = [b]
    l = max(l, a)
arr = [0] * l
for key in dic.keys():
    dic.get(key).sort(reverse=True)
    arr[key - 1] = dic.get(key)[0]
for i in reversed(range(len(arr))):
    if not dic.get(i + 1): continue
    for j in range(1, len(dic.get(i + 1))):
        target = dic.get(i + 1)[j]
        for k in reversed(range(i + 1)):
            if target > arr[k]:
                temp = arr[k]
                arr[k] = target
                target = temp
print(sum(arr))
