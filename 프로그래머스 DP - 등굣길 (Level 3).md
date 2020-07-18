## 프로그래머스 DP - 등굣길 (Level 3)

###### 문제 설명

계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

아래 그림은 m = 4, n = 3 인 경우입니다.

![image0.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/056f54e618/f167a3bc-e140-4fa8-a8f8-326a99e0f567.png)

가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
  - m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
- 물에 잠긴 지역은 0개 이상 10개 이하입니다.
- 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.

##### 입출력 예

| m    | n    | puddles  | return |
| ---- | ---- | -------- | ------ |
| 4    | 3    | [[2, 2]] | 4      |

##### 입출력 예 설명

![image1.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/32c67958d5/729216f3-f305-4ad1-b3b0-04c2ba0b379a.png)



출처 : https://programmers.co.kr/learn/courses/30/lessons/42898



---



#### My solution (Java)

```java
class Solution {
   public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[] arr = new int[m * n + 1];
        for (int i = 0; i < puddles.length; i++) {
            int puddleNode = puddles[i][0] + (puddles[i][1] - 1) * m;
            arr[puddleNode] = -1;
        }
        arr[1] = 1;
        for (int i = 1; i <= m * n; i++) {
            if (arr[i] != -1) {
                if (i % m != 0 && arr[i + 1] != -1) {
                    arr[i + 1] += arr[i] % 1000000007;
                }
                if (i + m <= m * n && arr[i + m] != -1) {
                    arr[i + m] += arr[i] % 1000000007;
                }
            }
        }
        answer = arr[m * n] % 1000000007;
        return answer;
    }
}
```



---

#### My logic & Feedback

Dynamic Programming과 길찾기가 결합된 가장 전형적인 문제라고 생각된다.

프로그래머스에 이와 비슷하지만 좀 더 업그레이드 된 문제는 **보행자 천국**이라는 문제인데,

(https://programmers.co.kr/learn/courses/30/lessons/1832)

보행자 천국은 테케가 실패로 떴다. 보행자 천국은 프로그래머스에 테케가 하나밖에 없어서 어디서 틀렸는지 알 수 없어 난감하다.

위 등굣길 문제는, 각 점에 도달하는 총 경우의 수를 모드 더해 다음 도달점(오른쪽 점 및 아래 점)에 넘기고, 넘기고, 하는 방식으로

맨 마지막 점까지 도달하면 맨 마지막점으로 오는 총 경우의 수가 나오므로 그 값을 반환하면 된다.

나는 처음에 HashMap 2개를 이용해서 풀었는데, **HashMap<Integer, HashMap<Integer, Integer>>** 라는 구조로 특정 점의 x, y 좌표를 저장하고 value에 경우의 수를 넣고자 했다.

x, y 가 각각의 HashMap의 Key를 의미하므로 다른 점으로 옮겨갈 때 해당 HashMap의 HashMap에 Value를 추가해주면 된다.

(이 방식으로 하면 시간복잡도는 단축되나 탐색 시 HashMap의 null처리가 까다롭다.)

그러나 정확도는 다 통과했는데 효율성이 모두 박살이 났고....

다시 배열을 통해 한 점의 id에 경우의 수를 담는 방식으로 변경하였다.

그래도 효율성이 모두 실패했다.....

도저히 원인을 모르겠어서 질문하기 게시판을 봤는데,

경우의 수를 계속 더해가는 과정에서 다음 점으로 넘길 경우의 수가 int 범위를 초과하기 때문에,

값을 넘길 때 마다 경우의 수를 Moduler 연산을 통해 나머지만 넘겨주어야 한다는 글을 봤다.

그리고 MOD 연산을 반영하므로서 효율성을 모두 통과하였다..아마 원래 쓰려고 했던 이중 HashMap으로도 Mod 연산을 했으면 통과하지 않았을까 싶다.

생각해보면, 더하기를 계속 하다가 맨 마지막에 나머지를 구하나, 더할 수를 미리 나누어서 나머지를 구한 후 마지막에 그 나머지의 나머지를 구하나 같은 방법임을 나중에서야 알 수 있었다.

(5+10) / 4 의 나머지는 ((5/4의 나머지) + (10/4)의 나머지))/4의 나머지 와 동일하므로...

문제는 전혀 어렵지 않았지만, Mod 연산에 대한 통찰을 배울 수 있는 좋은 문제였다.

