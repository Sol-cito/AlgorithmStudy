## Leetcode - Perfect Squares [Medium]

- Given a positive integer *n*, find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to *n*.

  **Example 1:**

  ```
  Input: n = 12
  Output: 3 
  Explanation: 12 = 4 + 4 + 4.
  ```

  **Example 2:**

  ```
  Input: n = 13
  Output: 2
  Explanation: 13 = 4 + 9.
  ```



Link : https://leetcode.com/problems/perfect-squares/

---



#### My solution (Java)

```java
class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 0;
        for (int i = 1; i * i <= n; i++) {
            int square = i * i;
            for (int j = 1; j <= n; j++) {
                dp[j] = i == 1 ? j : Math.min(j / square + dp[j - (square) * (j / square)], dp[j]);
            }
        }
        return dp[n];
    }
}
```

---



#### My logic & Feedback

전형적인 DP문제다.

풀이는 뭐..그냥 1차원 DP 배열을 계속 갱신해나가면 되는데,

1~n까지의 수가 각 square 넘버로 **'필요한 가장 최소값이 얼마인지'**를 갱신해나간다.

예를들어 n=12일 때, 가장 작은 square 수인 1부터 시작하면 dp[1~12]는 1,2,3,...12 가 된다.

다음 square 수인 4는 dp[1~3]까지는 1,2,3 으로 동일하지만, dp[4] = 1, dp[5] = 2, dp[6] = 3...이런식으로 값이 줄어든다.

Math.min 메소드를 통해 dp값을 갱신해나가다가,

다 끝나고 맨 마지막 element를 return하면 끝~~~