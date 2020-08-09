## 프로그래머스 블록 이동하기 - 2020 Kakao blind (Level 3)

###### 문제 설명

로봇개발자 **무지**는 한 달 앞으로 다가온 카카오배 로봇경진대회에 출품할 **로봇**을 준비하고 있습니다. 준비 중인 로봇은 **`2 x 1`** 크기의 로봇으로 무지는 **0**과 **1**로 이루어진 **`N x N`** 크기의 지도에서 **`2 x 1`** 크기인 로봇을 움직여 **(N, N)** 위치까지 이동 할 수 있도록 프로그래밍을 하려고 합니다. 로봇이 이동하는 지도는 가장 왼쪽, 상단의 좌표를 **(1, 1)**로 하며 지도 내에 표시된 숫자 **0**은 빈칸을 **1**은 벽을 나타냅니다. 로봇은 벽이 있는 칸 또는 지도 밖으로는 이동할 수 없습니다. 로봇은 처음에 아래 그림과 같이 좌표 **(1, 1)** 위치에서 가로방향으로 놓여있는 상태로 시작하며, 앞뒤 구분없이 움직일 수 있습니다.

![블럭이동-1.jpg](https://grepp-programmers.s3.amazonaws.com/files/production/33f5c19ba6/052d3514-5fca-4b85-82aa-0f9eaefae0a3.jpg)

로봇이 움직일 때는 현재 놓여있는 상태를 유지하면서 이동합니다. 예를 들어, 위 그림에서 오른쪽으로 한 칸 이동한다면 **(1, 2), (1, 3)** 두 칸을 차지하게 되며, 아래로 이동한다면 **(2, 1), (2, 2)** 두 칸을 차지하게 됩니다. 로봇이 차지하는 두 칸 중 어느 한 칸이라도 **(N, N)** 위치에 도착하면 됩니다.

로봇은 다음과 같이 조건에 따라 회전이 가능합니다.

![블럭이동-2.jpg](https://grepp-programmers.s3.amazonaws.com/files/production/edfcdf57d3/f87055df-91e5-4f47-b99a-400c54bfdf3a.jpg)

위 그림과 같이 로봇은 90도씩 회전할 수 있습니다. 단, 로봇이 차지하는 두 칸 중, 어느 칸이든 축이 될 수 있지만, 회전하는 방향(축이 되는 칸으로부터 대각선 방향에 있는 칸)에는 벽이 없어야 합니다. 로봇이 한 칸 이동하거나 90도 회전하는 데는 걸리는 시간은 정확히 1초 입니다.

**0**과 **1**로 이루어진 지도인 board가 주어질 때, 로봇이 **(N, N)** 위치까지 이동하는데 필요한 최소 시간을 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- board의 한 변의 길이는 5 이상 100 이하입니다.
- board의 원소는 0 또는 1입니다.
- 로봇이 처음에 놓여 있는 칸 (1, 1), (1, 2)는 항상 0으로 주어집니다.
- 로봇이 항상 목적지에 도착할 수 있는 경우만 입력으로 주어집니다.

------

### 입출력 예

| board                                                        | result |
| ------------------------------------------------------------ | ------ |
| [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]] | 7      |

### 입출력 예에 대한 설명

문제에 주어진 예시와 같습니다.
로봇이 오른쪽으로 한 칸 이동 후, (1, 3) 칸을 축으로 반시계 방향으로 90도 회전합니다. 다시, 아래쪽으로 3칸 이동하면 로봇은 (4, 3), (5, 3) 두 칸을 차지하게 됩니다. 이제 (5, 3)을 축으로 시계 방향으로 90도 회전 후, 오른쪽으로 한 칸 이동하면 (N, N)에 도착합니다. 따라서 목적지에 도달하기까지 최소 7초가 걸립니다.

출처 : https://programmers.co.kr/learn/courses/30/lessons/60063





---

#### My first solution (Java) 

```java
import java.util.LinkedList;
import java.util.Queue;

class Solution {
 public int solution(int[][] board) {
        int answer = 0;

        /* nodeId 배열 생성*/
        int[][] nodeId = new int[board.length][board.length];
        int nodeIdCount = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                nodeId[i][j] = nodeIdCount;
                nodeIdCount++;
            }
        }

        /* queue 생성 후 첫 값 넣어주기 */
        Queue<DroneMove> que = new LinkedList<>();
        int[][] visitCheck = new int[nodeIdCount][nodeIdCount];
        visitCheck[nodeId[0][1]][nodeId[0][0]] = 1;
        DroneMove firstMove = new DroneMove(0, 1, 0, 0, 1, 0);
        que.add(firstMove);

        /* 이동 방향 배열 */
        int[][] updownbackforth = {{0, -1, 0, -1}, {0, 1, 0, 1}, {-1, 0, -1, 0}, {1, 0, 1, 0}}; // 상하좌우

        /* Loop start */
        while (!que.isEmpty()) {
            DroneMove polledDrone = que.poll();
            if (polledDrone.head_x == board.length - 1 && polledDrone.head_y == board.length - 1) {
                answer = polledDrone.count;
                break;
            }

            for (int i = 0; i < updownbackforth.length; i++) { // 상하좌우 이동
                int nextHead_x = polledDrone.head_x + updownbackforth[i][0];
                int nextHead_y = polledDrone.head_y + updownbackforth[i][1];
                int nextTail_x = polledDrone.tail_x + updownbackforth[i][2];
                int nextTail_y = polledDrone.tail_y + updownbackforth[i][3];
                if (checkValidity(nextHead_x, nextHead_y, nextTail_x, nextTail_y, board, nodeId, visitCheck)) {
                    DroneMove newMove = new DroneMove(nextHead_x, nextHead_y, nextTail_x, nextTail_y, polledDrone.status, polledDrone.count + 1);
                    que.add(newMove);
                    visitCheck[nodeId[nextHead_x][nextHead_y]][nodeId[nextTail_x][nextTail_y]] = 1;
                }
            }
            if (polledDrone.status == 1) { // 가로면
                int[][] down = {{1, -1, 0, 0}, {1, 0, 0, 1}}; // 아래로 회전
                for (int i = 0; i < down.length; i++) {
                    int nextHead_x = polledDrone.head_x + down[i][0];
                    int nextHead_y = polledDrone.head_y + down[i][1];
                    int nextTail_x = polledDrone.tail_x + down[i][2];
                    int nextTail_y = polledDrone.tail_y + down[i][3];
                    if (checkValidity(nextHead_x, nextHead_y, nextTail_x, nextTail_y, board, nodeId, visitCheck)
                            && checkDiagonal(polledDrone.head_x + 1, polledDrone.head_y, polledDrone.tail_x + 1, polledDrone.tail_y, board)) {
                        DroneMove newMove = new DroneMove(nextHead_x, nextHead_y, nextTail_x, nextTail_y, 2, polledDrone.count + 1);
                        que.add(newMove);
                        visitCheck[nodeId[nextHead_x][nextHead_y]][nodeId[nextTail_x][nextTail_y]] = 1;
                    }
                }
                int[][] up = {{0, 0, -1, 1}, {0, -1, -1, 0}}; // 위로 회전
                for (int i = 0; i < up.length; i++) {
                    int nextHead_x = polledDrone.head_x + up[i][0];
                    int nextHead_y = polledDrone.head_y + up[i][1];
                    int nextTail_x = polledDrone.tail_x + up[i][2];
                    int nextTail_y = polledDrone.tail_y + up[i][3];
                    if (checkValidity(nextHead_x, nextHead_y, nextTail_x, nextTail_y, board, nodeId, visitCheck)
                            && checkDiagonal(polledDrone.head_x - 1, polledDrone.head_y, polledDrone.tail_x - 1, polledDrone.tail_y, board)) {
                        DroneMove newMove = new DroneMove(nextHead_x, nextHead_y, nextTail_x, nextTail_y, 2, polledDrone.count + 1);
                        que.add(newMove);
                        visitCheck[nodeId[nextHead_x][nextHead_y]][nodeId[nextTail_x][nextTail_y]] = 1;
                    }
                }
            } else { // 세로면
                int[][] right = {{0, 1, 1, 0}, {-1, 1, 0, 0}}; // 오른쪽으로 회전
                for (int i = 0; i < right.length; i++) {
                    int nextHead_x = polledDrone.head_x + right[i][0];
                    int nextHead_y = polledDrone.head_y + right[i][1];
                    int nextTail_x = polledDrone.tail_x + right[i][2];
                    int nextTail_y = polledDrone.tail_y + right[i][3];
                    if (checkValidity(nextHead_x, nextHead_y, nextTail_x, nextTail_y, board, nodeId, visitCheck)
                            && checkDiagonal(polledDrone.head_x, polledDrone.head_y + 1, polledDrone.tail_x, polledDrone.tail_y + 1, board)) {
                        DroneMove newMove = new DroneMove(nextHead_x, nextHead_y, nextTail_x, nextTail_y, 1, polledDrone.count + 1);
                        que.add(newMove);
                        visitCheck[nodeId[nextHead_x][nextHead_y]][nodeId[nextTail_x][nextTail_y]] = 1;
                    }
                }
                int[][] left = {{0, 0, 1, -1}, {-1, 0, 0, -1}}; // 왼쪽으로 회전
                for (int i = 0; i < left.length; i++) {
                    int nextHead_x = polledDrone.head_x + left[i][0];
                    int nextHead_y = polledDrone.head_y + left[i][1];
                    int nextTail_x = polledDrone.tail_x + left[i][2];
                    int nextTail_y = polledDrone.tail_y + left[i][3];
                    if (checkValidity(nextHead_x, nextHead_y, nextTail_x, nextTail_y, board, nodeId, visitCheck)
                            && checkDiagonal(polledDrone.head_x, polledDrone.head_y - 1, polledDrone.tail_x, polledDrone.tail_y - 1, board)) {
                        DroneMove newMove = new DroneMove(nextHead_x, nextHead_y, nextTail_x, nextTail_y, 1, polledDrone.count + 1);
                        que.add(newMove);
                        visitCheck[nodeId[nextHead_x][nextHead_y]][nodeId[nextTail_x][nextTail_y]] = 1;
                    }
                }
            }
        }
        return answer;
    }

    public boolean checkDiagonal(int head_x, int head_y, int tail_x, int tail_y, int[][] board) {
        if (board[head_x][head_y] == 0 && board[tail_x][tail_y] == 0) {
            return true;
        }
        return false;
    }

    public boolean checkValidity(int head_x, int head_y, int tail_x, int tail_y, int[][] board,
                                 int[][] nodeId, int[][] visitCheck) {
        if (head_x >= 0 && head_x < board.length && head_y >= 0 && head_y < board.length
                && tail_x >= 0 && tail_x < board.length && tail_y >= 0 && tail_y < board.length
                && board[head_x][head_y] == 0 && board[tail_x][tail_y] == 0
                && visitCheck[nodeId[head_x][head_y]][nodeId[tail_x][tail_y]] == 0) {
            return true;
        }
        return false;
    }
}

class DroneMove {
    int head_x;
    int head_y;
    int tail_x;
    int tail_y;
    int status;
    int count;

    public DroneMove(int head_x, int head_y, int tail_x, int tail_y, int status, int count) {
        this.head_x = head_x;
        this.head_y = head_y;
        this.tail_x = tail_x;
        this.tail_y = tail_y;
        this.status = status;
        this.count = count;
    }
}

```





---

#### My logic & feedback

악마의 카카오 문제...

복잡한 로직 없이 오로지 '구현력'을 보는 문제로, 문제에서 제시한 대로 충실히 BFS를 구현하면 풀리는 문제다.

그 구현하는게 짜증나서 그렇지...

문제의 핵심은 head와 tail이라는 2개의 변수를 한꺼번에 생각해야한다는 점과,

visitCheck를 할 때 head_x, head_y, tail_x, tail_y 라는 4개의 요소로 visitCheck를 해야한다는 점이다.

나는 nodeID라는 2차원 배열을 만들고 각 element에 0부터 1씩 증가하는 숫자를 넣어서,

x,y값을 넣었을 때 유일한 integer를 잡을 수 있도록 구현했다.

즉 visitCheck라는 2차원 배열에 들어갈 x,y값을 또 다른 2차원 배열에서 가져오는 방식이다.

이 방법은 꽤나 간단하면서도 효과적이기 때문에, 다음 문제를 풀 때도 잘 써먹어야겠다.

처음에 큐를 구현할 때 각 Move에 visitCheck 배열을 넣어 새로운 배열로 복사한 뒤 queue에 넣는 방식을 썼는데,

시간초과가 났다.

생각해보니 BFS는 global member 변수로 visitCheck를 하나만 생성해도 상관없다. DFS는 움직일 때 마다 visitCheck를 해주어야 하지만..

이 문제는 사실 세 달 전에 스터디에서 풀이를 시도했다가 실패하고,

그 이후에 한 번 더 시도했다가 실패하고,

이제 드디어 풀어낸 문제인데, 속이 너무 시원하다.