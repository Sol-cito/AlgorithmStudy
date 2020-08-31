## Leetcode - Minimum Path Sum [Medium]

Given a *m* x *n* grid filled with non-negative numbers, find a path from top left to bottom right which *minimizes* the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

**Example:**

```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

Link : https://leetcode.com/problems/minimum-path-sum/



---



#### My solution (Java)

```java
class Solution {
     public int minPathSum(int[][] grid) {
        int cnt = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (cnt != 0) {
                    int nextValue = Integer.MAX_VALUE;
                    if (i - 1 >= 0) {
                        nextValue = Math.min(nextValue, grid[i - 1][j]);
                    }
                    if (j - 1 >= 0) {
                        nextValue = Math.min(nextValue, grid[i][j - 1]);
                    }
                    grid[i][j] = grid[i][j] + nextValue;
                }
                cnt++;
            }
        }
        return grid[grid.length - 1][grid[0].length - 1];
    }
}
```

---



#### My logic & Feedback

Grid 위에서 오른쪽, 아래쪽으로밖에 움직일 수 없다.

따라서 Grid의 한 점은 자신의 왼쪽 or 위쪽의 점에서 가장 작은 수를 선택하여 본인이 가진 value와 더해주면 된다.

즉 Dynamic Programming + Greedy의 방식으로 끝 지점이 가질 수 있는 최소값을 구했다.