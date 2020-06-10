## 프로그래머스 외벽 점검 - 2020 KAKAO Blind Recruitment (Level 3)

###### 문제 설명

레스토랑을 운영하고 있는 **스카피**는 레스토랑 내부가 너무 낡아 친구들과 함께 직접 리모델링 하기로 했습니다. 레스토랑이 있는 곳은 스노우타운으로 매우 추운 지역이어서 내부 공사를 하는 도중에 주기적으로 외벽의 상태를 점검해야 할 필요가 있습니다.

레스토랑의 구조는 **완전히 동그란 모양**이고 **외벽의 총 둘레는 n미터**이며, 외벽의 몇몇 지점은 추위가 심할 경우 손상될 수도 있는 **취약한 지점들**이 있습니다. 따라서 내부 공사 도중에도 외벽의 취약 지점들이 손상되지 않았는 지, 주기적으로 친구들을 보내서 점검을 하기로 했습니다. 다만, 빠른 공사 진행을 위해 점검 시간을 1시간으로 제한했습니다. 친구들이 1시간 동안 이동할 수 있는 거리는 제각각이기 때문에, 최소한의 친구들을 투입해 취약 지점을 점검하고 나머지 친구들은 내부 공사를 돕도록 하려고 합니다. 편의 상 레스토랑의 정북 방향 지점을 0으로 나타내며, 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리로 나타냅니다. 또, 친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동합니다.

외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist가 매개변수로 주어질 때, 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값을 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- n은 1 이상 200 이하인 자연수입니다.
- weak의 길이는 1 이상 15 이하입니다.
  - 서로 다른 두 취약점의 위치가 같은 경우는 주어지지 않습니다.
  - 취약 지점의 위치는 오름차순으로 정렬되어 주어집니다.
  - weak의 원소는 0 이상 n - 1 이하인 정수입니다.
- dist의 길이는 1 이상 8 이하입니다.
  - dist의 원소는 1 이상 100 이하인 자연수입니다.
- 친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우에는 -1을 return 해주세요.

------

### 입출력 예

| n    | weak             | dist         | result |
| ---- | ---------------- | ------------ | ------ |
| 12   | [1, 5, 6, 10]    | [1, 2, 3, 4] | 2      |
| 12   | [1, 3, 4, 9, 10] | [3, 5, 7]    | 1      |

### 입출력 예에 대한 설명

**입출력 예 #1**

원형 레스토랑에서 외벽의 취약 지점의 위치는 다음과 같습니다.

![외벽점검-1.jpg](https://grepp-programmers.s3.amazonaws.com/files/production/61de504978/1c8394ec-05e0-4b7b-a0ff-3ff9ae0cec28.jpg)

친구들을 투입하는 예시 중 하나는 다음과 같습니다.

- 4m를 이동할 수 있는 친구는 10m 지점에서 출발해 시계방향으로 돌아 1m 위치에 있는 취약 지점에서 외벽 점검을 마칩니다.
- 2m를 이동할 수 있는 친구는 4.5m 지점에서 출발해 6.5m 지점에서 외벽 점검을 마칩니다.

그 외에 여러 방법들이 있지만, 두 명보다 적은 친구를 투입하는 방법은 없습니다. 따라서 친구를 최소 두 명 투입해야 합니다.

**입출력 예 #2**

원형 레스토랑에서 외벽의 취약 지점의 위치는 다음과 같습니다.

![외벽점검-2.jpg](https://grepp-programmers.s3.amazonaws.com/files/production/3669c9b3d6/00e8eeb4-f3ec-4c18-96fb-a3b17aaf1812.jpg)

7m를 이동할 수 있는 친구가 4m 지점에서 출발해 반시계 방향으로 점검을 돌면 모든 취약 지점을 점검할 수 있습니다. 따라서 친구를 최소 한 명 투입하면 됩니다.



출처 : https://programmers.co.kr/learn/courses/30/lessons/60062



---

#### My first solution (Java)

```java
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
     int result = -1;

    public int solution(int n, int[] weak, int[] dist) {
        int answer = 0;
        Arrays.sort(dist);
        recursion(n, weak, dist, dist.length - 1, 0);
        answer = result;
        return answer;
    }

    public void recursion(int n, int[] weak, int[] dist, int distIndex, int count) {
        if (distIndex < 0 && weak.length != 0) {
            return;
        }
        if (weak.length == 0) {
            if (result == -1) {
                result = count;
            } else {
                result = Math.min(result, count);
            }
            return;
        }
        int pickedDist = dist[distIndex];
        int[] doubleWeak = new int[weak.length * 2];
        for (int i = 0; i < doubleWeak.length; i++) {
            if (i < weak.length) {
                doubleWeak[i] = weak[i];
            } else {
                doubleWeak[i] = weak[i - weak.length] + n;
            }
        }
        for (int i = 0; i < weak.length; i++) {
            Queue<Integer> que = new LinkedList<>();
            int pointer = i;
            while (que.size() < weak.length) {
                que.add(doubleWeak[pointer]);
                pointer++;
            }
            int distanceOfTwoPolled = pickedDist;
            int firstPoll = que.poll();
            while (!que.isEmpty() && distanceOfTwoPolled >= que.peek() - firstPoll) {
                int peeked = que.peek();
                distanceOfTwoPolled -= (peeked - firstPoll);
                firstPoll = que.poll();
            }
            int[] newWeak = new int[que.size()];
            int index = 0;
            while (!que.isEmpty()) {
                newWeak[index] = que.poll();
                index++;
            }
            recursion(n, newWeak, dist, distIndex - 1, count + 1);
        }
    }
}
```

---

#### My logic & feedback

#####  재귀와 Queue를 이용..하여 통과는 하였으나 효율성이 떨어진다.

아래에 위 코드의 결과가 나타나있다.

![image-20200610232213081](C:\Users\datae\AppData\Roaming\Typora\typora-user-images\image-20200610232213081.png)



효율성 테스트가 없었기에 망정이지, 테스트 13번 같은 경우는 통과가 간당간당한 수준이었다.

문제를 일부러 연산속도가 저렇게 나오도록 냈을 리는 없고, 분명히 더 효과적인 방법이 있을텐데 내가 그것을 발견하지 못했을 것이다.

어쨌든 나의 풀이로직은 다음과 같다.



문제풀이의 핵심은 **'가장 많은 거리(dist)를 갈 수 있는 친구가 가장 많은 외벽(weak)을 점검해야 한다'**라고 생각했다.

따라서,

1. int[] dist 를 정렬하여 가장 많은 거리를 갈 수 있는 친구를 찾는다.

2. 외벽점검은 좌, 우 양방향으로 할 수 있기에 weak배열로부터 doubleWeak 배열을 만든다

   --> n이 12, weak가 {1, 5, 6, 10} 이라면 doubleWeak는 {1, 5, 6, 10, 13(1), 17(5), 18(6), 22(10) } 가 되며,

   이 doubleWeak를 weak의 범위만큼 탐색하며 가장 많은 거리를 갈 수 있는 친구가 지울 수 있는 가장 많은 weak의 경우를 찾는다.

3. 이 때, 각 weak는 Queue를 활용하며, polled된 weak를 제외한 나머지 integer들을 다시 다른 배열(newWeak)에 담아 재귀적으로 다음 턴으로 넘긴다.

4. 이렇게 재귀를 반복하다가, 만약 아직 newWeak에 integer가 남아있는데도(즉, 아직 외벽점검이 다 끝나지 않았는데도) dist 배열의 탐색이 끝났다면 -> -1을 반환한다.

5. 반면 newWeak의 길이가 0이라면(즉, 외벽점검이 다 끝났다면), 여태까지 재귀가 돌았던 count를 반환하면 된다.

6. 만약 count를 하나 이상이라도 반환하였다면 답은 반환한 count 중 가장 작은 값이 될 것이고, 그렇지 않다면 -1이 될 것이다.



#### Feedback

이 문제는 내가 고른 문제였으나...Level 3 치고는 풀이방법 및 구현을 생각해내는 데 상당히 오랜시간이 소요되었다(더구나 연산시간도 오래 소요되었다..).

분명히 더 기발하고 효율적인 방법이 있을테니, 내일 스터디 때 스터디원들과 토론해보고 다시 다른방법으로 풀어봐야겠다.