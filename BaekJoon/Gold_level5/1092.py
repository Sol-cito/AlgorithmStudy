import sys

N = int(sys.stdin.readline())
cranes = sorted(list(map(int, sys.stdin.readline().split(" "))), reverse=True)
boxNum = int(sys.stdin.readline())
boxes = sorted(list(map(int, sys.stdin.readline().split(" "))), reverse=True)
res = cnt = 0
if cranes[0] < boxes[0]:
    print(-1)
    exit()
visit = [0 for i in range(boxNum)]
while cnt < boxNum:
    for crane in cranes:
        flag = False
        for i in range(len(boxes)):
            if visit[i] == 0 and crane >= boxes[i]:
                visit[i] = 1
                cnt += 1
                flag = True
                break
        if not flag:
            cranes.remove(crane)
    res += 1
print(res)