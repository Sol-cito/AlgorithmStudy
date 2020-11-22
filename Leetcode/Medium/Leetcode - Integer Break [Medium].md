## Leetcode - Integer Break [Medium]

Given a positive integer *n*, break it into the sum of **at least** two positive integers and maximize the product of those integers. Return the maximum product you can get.

**Example 1:**

```
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
```

**Example 2:**

```
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
```

**Note**: You may assume that *n* is not less than 2 and not larger than 58.

Link : https://leetcode.com/problems/integer-break/



---



#### My solution (Java)

```java
class Solution {
    public int integerBreak(int n) {
        int[] dp = new int[n];
        dp[0] = dp[1] = 1;
        for (int i = 2; i < n; i++) {
            dp[i - 1] = Math.max(dp[i - 1], i);
            for (int j = 1; j < i; j++) {
                dp[i] = Math.max(dp[i], dp[i - j] * j);
            }
        }
        return dp[n - 1];
    }
}
```

---



#### My logic & Feedback

간단한 DP문제. 다른 풀이법이 있는지는 모르겠다.

input이 10일때를 예로 들면, 

10은 Math.max( (1이 input일때의 값 * 9) , (2가 input일 때의 값 * 8), (3이 input일 때의 값 * 7) ....) 으로 나타낼 수 있다.

즉, 점화식은

```
f(1) = 1
f(n) = Math.max ( f(1) * (n - 1), f(2) * (n - 2), f(3) * (n - 3) , ..., f(n - 1))
```

이 된다. 

주의할 점은, dp배열을 한번 갱신할 때 마다 dp[i - 1] = Math.max(dp[i - 1], i); 식을 통해서 자신의 바로 뒤 배열값을 조절해주어야 한다는 점이다.

가령 3의 경우, 가장 큰 값은 1 * 2 = 2 지만, 4를 만들 때 3 * 1 = 3 의 값이 경우의 수 중 하나가 될 수 있으므로 이 경우 dp[3] = 3 이 되어야 한다. 

따라서 dp배열의 갱신이 일어날 때마다 본인의 값과 dp배열값을 max비교로 갱신해주면 된다.