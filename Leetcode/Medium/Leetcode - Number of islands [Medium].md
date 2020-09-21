## Leetcode - Number of islands [Medium]

Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

**Example 1:**

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

Link : https://leetcode.com/problems/number-of-islands/submissions/

---



#### My solution (Java)

```java
class Solution {
     public int numIslands(char[][] grid) {
        int answer = 0;
        if (grid.length == 0 || grid[0].length == 0) {
            return answer;
        }
        int[][] visitArr = new int[grid.length][grid[0].length];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (visitArr[i][j] == 0 && grid[i][j] == '1') {
                    checkIsland(grid, i, j, visitArr);
                    answer++;
                }
                visitArr[i][j] = 1;
            }
        }
        return answer;
    }

    public void checkIsland(char[][] grid, int x, int y, int[][] visitArr) {
        int[][] direction = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (int i = 0; i < direction.length; i++) {
            int nextX = x + direction[i][0];
            int nextY = y + direction[i][1];
            if (nextX >= 0 && nextX < grid.length && nextY >= 0 && nextY < grid[0].length
                    && grid[nextX][nextY] == '1' && visitArr[nextX][nextY] == 0) {
                visitArr[nextX][nextY] = 1;
                checkIsland(grid, nextX, nextY, visitArr);
            }
        }
    }
}

```

---



#### My logic & Feedback

재귀를 이용한 DFS로 간단히 풀 수 있는 문제다.

1인 grid를 만나면 visit 하지 않은 것 중 상하좌우의 grid를 탐색하여 하나의 섬을 전부 탐색한다.

재귀가 끝나면 for문으로 돌아가는데, 재귀에서 반영된 visitArr때문에 이미 탐색한 grid는 skip하게 된다.