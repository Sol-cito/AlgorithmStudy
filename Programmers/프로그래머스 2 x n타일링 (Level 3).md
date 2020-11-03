## 프로그래머스 2 x n타일링 (Level 3)

###### 문제 설명

가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있습니다. 이 직사각형 타일을 이용하여 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다. 타일을 채울 때는 다음과 같이 2가지 방법이 있습니다.

- 타일을 가로로 배치 하는 경우
- 타일을 세로로 배치 하는 경우

예를들어서 n이 7인 직사각형은 다음과 같이 채울 수 있습니다.

![Imgur](https://i.imgur.com/29ANX0f.png)

직사각형의 가로의 길이 n이 매개변수로 주어질 때, 이 직사각형을 채우는 방법의 수를 return 하는 solution 함수를 완성해주세요.

##### 제한사항

- 가로의 길이 n은 60,000이하의 자연수 입니다.
- 경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.

------

##### 입출력 예

| n    | result |
| ---- | ------ |
| 4    | 5      |

##### 입출력 예 설명

입출력 예 #1
다음과 같이 5가지 방법이 있다.

![Imgur](https://i.imgur.com/keiKrD3.png)

![Imgur](https://i.imgur.com/O9GdTE0.png)

![Imgur](https://i.imgur.com/IZBmc6M.png)

![Imgur](https://i.imgur.com/29LWVzK.png)

![Imgur](https://i.imgur.com/z64JbNf.png)

출처 : https://programmers.co.kr/learn/courses/30/lessons/12900

---

#### My solution (Java)

  ```
class Solution {
    public int solution(int n) {
        if(n == 1) return 1;
        int[] dp = new int[n];
        dp[0] = 1;
        dp[1] = 2;
        for(int i = 2; i < n; i++){
            dp[i] = dp[i - 1]%1000000007 + dp[i - 2]%1000000007;
        }
        return dp[n-1]%1000000007;
    }
}
  ```



---

#### My logic & Feedback

처음에 헤메다가, DP를 배우고 나서 바로 풀이에 성공한 문제.

Dynamic Programming으로 풀지 않으면 시간초과가 날 것 같다.

문제를 DP로 잘 생각해보면...그냥 피보나치다.