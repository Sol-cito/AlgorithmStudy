## 프로그래머스 기지국 설치 (Level 3) Summer Winter Coding(~2018)

###### 문제 설명

N개의 아파트가 일렬로 쭉 늘어서 있습니다. 이 중에서 일부 아파트 옥상에는 4g 기지국이 설치되어 있습니다. 기술이 발전해 5g 수요가 높아져 4g 기지국을 5g 기지국으로 바꾸려 합니다. 그런데 5g 기지국은 4g 기지국보다 전달 범위가 좁아, 4g 기지국을 5g 기지국으로 바꾸면 어떤 아파트에는 전파가 도달하지 않습니다.

예를 들어 11개의 아파트가 쭉 늘어서 있고, [4, 11] 번째 아파트 옥상에는 4g 기지국이 설치되어 있습니다. 만약 이 4g 기지국이 전파 도달 거리가 1인 5g 기지국으로 바뀔 경우 모든 아파트에 전파를 전달할 수 없습니다. (전파의 도달 거리가 W일 땐, 기지국이 설치된 아파트를 기준으로 전파를 양쪽으로 W만큼 전달할 수 있습니다.)

- 초기에, 1, 2, 6, 7, 8, 9번째 아파트에는 전파가 전달되지 않습니다.

![image](https://res.cloudinary.com/jistring93/image/upload/v1492073407/%EA%B8%B0%EC%A7%80%EA%B5%AD%EC%84%A4%EC%B9%981_pvskxt.png)

- 1, 7, 9번째 아파트 옥상에 기지국을 설치할 경우, 모든 아파트에 전파를 전달할 수 있습니다.

![image](https://res.cloudinary.com/jistring93/image/upload/v1492073617/%EA%B8%B0%EC%A7%80%EA%B5%AD%EC%84%A4%EC%B9%982_kml0pb.png)

- 3개의 아파트보다 더 많은 아파트 옥상에 기지국을 설치할 경우에도 모든 아파트에 전파를 전달할 수 있습니다.

![image](https://res.cloudinary.com/jistring93/image/upload/v1492073725/%EA%B8%B0%EC%A7%80%EA%B5%AD%EC%84%A4%EC%B9%983_xhv7r3.png)

이때, 우리는 기지국을 **최소로 설치**하면서 모든 아파트에 전파를 전달하려고 합니다. 위의 예시에선 최소 3개의 아파트 옥상에 기지국을 설치해야 모든 아파트에 전파를 전달할 수 있습니다.

아파트의 개수 N, 현재 기지국이 설치된 아파트의 번호가 담긴 1차원 배열 stations, 전파의 도달 거리 W가 매개변수로 주어질 때, 모든 아파트에 전파를 전달하기 위해 증설해야 할 기지국 개수의 최솟값을 리턴하는 solution 함수를 완성해주세요

##### 제한사항

- N: 200,000,000 이하의 자연수
- stations의 크기: 10,000 이하의 자연수
- stations는 오름차순으로 정렬되어 있고, 배열에 담긴 수는 N보다 같거나 작은 자연수입니다.
- W: 10,000 이하의 자연수

------

##### 입출력 예

| N    | stations | W    | answer |
| ---- | -------- | ---- | ------ |
| 11   | [4, 11]  | 1    | 3      |
| 16   | [9]      | 2    | 3      |

##### 입출력 예 설명

입출력 예 #1
문제의 예시와 같습니다

입출력 예 #2

- 초기에, 1~6, 12~16번째 아파트에는 전파가 전달되지 않습니다.

![image](https://res.cloudinary.com/jistring93/image/upload/v1492485920/%EA%B8%B0%EC%A7%80%EA%B5%AD%EC%84%A4%EC%B9%984_nqfrmm.png)

- 3, 6, 14번째 아파트 옥상에 기지국을 설치할 경우 모든 아파트에 전파를 전달할 수 있습니다.

![image](https://res.cloudinary.com/jistring93/image/upload/v1492486043/%EA%B8%B0%EC%A7%80%EA%B5%AD%EC%84%A4%EC%B9%985_zh4ebk.png)



출처 : https://programmers.co.kr/learn/courses/30/lessons/12979



---



#### My solution (Java)

```java

class Solution {
      public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int scope = w * 2 + 1;
        /* 첫 번째 scope */
        int start = stations[0] - w;
        int end = stations[0] + w;
        if (start < 1) {
            start = 1;
        }
        if (end > n) {
            end = n;
        }
        int target = start - 1;
        int quotient = target / scope;
        answer += quotient;
        int remainder = target % scope;
        if (remainder > 0) {
            answer++;
        }
        /* 2번 기지국부터 탐색 */
        for (int i = 1; i < stations.length; i++) {
            int nextStart = stations[i] - w;
            int nextEnd = stations[i] + w;
            if (nextStart < 1) {
                nextStart = 1;
            }
            if (nextEnd > n) {
                nextEnd = n;
            }
            if (end < nextStart) { // 두 범위가 분리되는 시점
                target = nextStart - end - 1;
                quotient = target / scope;
                answer += quotient;
                remainder = target % scope;
                if (remainder > 0) {
                    answer++;
                }
                start = nextStart;
                end = nextEnd;
            } else { // 두 범위 통합
                end = nextEnd;
            }
        }
        /* 마지막 scope */
        target = n - end;
        quotient = target / scope;
        answer += quotient;
        remainder = target % scope;
        if (remainder > 0) {
            answer++;
        }
        return answer;
    }
}
```



---

#### My logic & Feedback

처음엔 기지국의 영향이 미치는 범위의 배열에 1을 넣고, 아닌 부분은 0을 넣으며 배열 전체탐색으로 기지국 수를 계산하려 하였다.

그러나 배열 길이가 2억개(...)라는 조건이 있었기에 효율성 테스트를 통과하지 못했고, 

배열을 하나씩 체크하는 방식으로는 효율성 테스트를 절대 통과하지 못할거라는 감이 와서 다른 방식을 고안했다.

핵심은, 기지국 배열 stations가 '오름차순'으로 정렬되어 있다는 점이다.

따라서 기지국의 영향 범위를 '작은 것 부터 순서대로' 파악하며 범위가 겹치면 그 영향 범위를 통째로 하나로 잡고, 영향 범위가 분리된다면 그 사이 빈 공간의 넓이를 캐치하면 된다.

기지국 배열이 오름차순 정렬이 되어있지 않다면 이 방법은 불가능할 것이다.

기지국의 영향범위 사이 빈 공간이 생겼을 때, 그 공간에 최소 몇 개의 기지국이 필요한지는 '몫과 나머지'를 이용해 계산하였다.