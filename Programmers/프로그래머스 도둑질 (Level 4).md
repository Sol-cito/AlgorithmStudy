## 프로그래머스 도둑질 (Level 4)

###### 문제 설명

도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.

![image.png](https://grepp-programmers.s3.amazonaws.com/files/ybm/e7dd4f51c3/a228c73d-1cbe-4d59-bb5d-833fd18d3382.png)

각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.

##### 제한사항

- 이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
- money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.

##### 입출력 예

| money        | return |
| ------------ | ------ |
| [1, 2, 3, 1] | 4      |



- 출처 : https://programmers.co.kr/learn/courses/30/lessons/42897

---

#### My solution (Java)

  ```
class Solution {
    public int solution(int[] money) {
        if (money.length == 3) return Math.max(Math.max(money[0], money[1]), money[2]);
        int answer = 0;
        int[] clone = money.clone();
        money[3] += money[1];
        clone[2] += clone[0];
        answer = Math.max(money[3], clone[2]);
        
        for (int i = 4; i < money.length; i++) {
            money[i] += Math.max(money[i - 2], money[i - 3]);
            clone[i - 1] += Math.max(clone[i - 3], clone[i - 4]);
            answer = Math.max(answer, Math.max(money[i], clone[i - 1]));
        }
        return answer;
    }
}
  ```



---

#### My logic & Feedback

기본적으로 DP문제고, Level 4의 수준은 절대 아니다...한 level 2~3 사이 정도의 난이도?

일단 주어진 length가 3 이하면, 그냥 가장 큰 수를 반환한다.

아니라면, 세 번째 배열은 += [첫 번째 배열 element]을 해 주고,

i가 4 이상일 경우

```
money(n) += max(money(n - 2), money(n - 3))
```

의 식을 생각해볼 수 있다.

위 식은 DP의 점화식은 아니나, money 배열의 element를 계속 갱신해나가는 방법이다.

또한, 집이 일렬이 아니라 원형이므로, 우리는 

**첫 번째 집을 반드시 털 경우(맨 마지막 집을 털지 않음)** 와

**마지막 집을 반드시 털 경우(맨 첫번째 집을 털지 않음)**를 고려해야 한다.

따라서 clone으로 배열을 하나 더 만들어서 for문 안에 넣고 같이 돌리면서 answer 값을 갱신해나간다.

내 풀이는 조금 변칙적인 DP라고 할 수 있겠는데,

다른 사람들 풀이를 보니, 그냥 정석적으로

int[] dp 를 만든 후,

```
dp[i] = Math.max(dp[i - 2] + money[i], dp[i - 1]);
```

의 점화식으로 푼 것 같다.

O(N)으로 집들을 탐색하되, 자신의 바로 옆 집은 도둑질하지 못하므로 +money[i]를 하지 않는 것이다.

사실 정석적인 점화식이 훨씬 직관적이고 깔끔하긴 하다.

