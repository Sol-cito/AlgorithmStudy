## Leetcode - Spiral Matrix ll [Medium]

Given a positive integer *n*, generate a square matrix filled with elements from 1 to *n*2 in spiral order.

**Example:**

```
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```

Link : https://leetcode.com/problems/spiral-matrix-ii/



---



#### My solution (Java)

```java
class Solution {
   public int[][] generateMatrix(int n) {
        int[][] answer = new int[n][n];
        int rangeStart = 0;
        int rageEnd = n - 1;

        int num = 1;
        while (rangeStart <= rageEnd) {
            for (int i = rangeStart; i <= rageEnd; i++) {
                answer[rangeStart][i] = num;
                num++;
            }
            for (int i = rangeStart + 1; i < rageEnd; i++) {
                answer[i][rageEnd] = num;
                num++;
            }
            for (int i = rageEnd; i >= rangeStart + 1; i--) {
                answer[rageEnd][i] = num;
                num++;
            }
            for (int i = rageEnd; i >= rangeStart + 1; i--) {
                answer[i][rangeStart] = num;
                num++;
            }
            rangeStart++;
            rageEnd--;
        }
        return answer;
    }
}

```

---



#### My logic & Feedback

Spiral Matrix 1 보다 더 쉬운 문제. 착실히 구현만 하면 풀린다.