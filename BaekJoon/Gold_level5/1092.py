import sys

#  크레인과 boxes 를 정렬한 후, 박스를 옮길 수 있는 크레인 중 가장 작업량이 한가한 크레인에 box를 할당한다.
#  그리고 작업 스케쥴에 있는 크레인 중 가장 횟수가 많은 것을 반환
N = int(sys.stdin.readline())
cranes = sorted(list(map(int, sys.stdin.readline().split(" "))), reverse=True)
boxNum = int(sys.stdin.readline())
boxes = sorted(list(map(int, sys.stdin.readline().split(" "))), reverse=True)
if cranes[0] < boxes[0]:
    print(-1)
    exit()
# 크레인 작업 스케쥴
craneSchedule = [0 for i in range(N)]
for box in boxes:
    idx, capa = 0, craneSchedule[0]
    for i in range(len(cranes)):
        if box <= cranes[i] and craneSchedule[i] <= capa:
            idx = i
            capa = craneSchedule[i]
        elif box > cranes[i]:
            break
    craneSchedule[idx] = capa + 1
print(max(craneSchedule))
