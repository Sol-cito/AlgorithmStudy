## Leetcode - Set Matrix Zeroes [Medium]

Given an `*m* x *n*` matrix. If an element is **0**, set its entire row and column to **0**. Do it [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm).

**Follow up:**

- A straight forward solution using O(*m**n*) space is probably a bad idea.
- A simple improvement uses O(*m* + *n*) space, but still not the best solution.
- Could you devise a constant space solution?

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

 

**Constraints:**

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-10^9 <= matrix[i][j] <= 10^9`

Link : https://leetcode.com/problems/set-matrix-zeroes/



---



#### My solution (Java)

```java
class Solution {
      public void setZeroes(int[][] matrix) {
        int[][] checkArr = new int[matrix.length][matrix[0].length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    checkArr[i][j] = -1;
                }
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (checkArr[i][j] == -1) {
                    swithToZero(matrix, i, j, checkArr);
                }
            }
        }

    }

    public void swithToZero(int[][] matrix, int x, int y, int[][] checkArr) {
        for (int i = 0; i < matrix[0].length; i++) {
            if (checkArr[x][i] != -1 && matrix[x][i] != 0) {
                matrix[x][i] = 0;
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            if (checkArr[i][y] != -1 && matrix[i][y] != 0) {
                matrix[i][y] = 0;
            }
        }
    }
}
```

---



#### My logic & Feedback

반복문만 적절히 잘 이용하면 풀리는 쉬운 문제.

문제의 포인트는 애초에 0인 spot과 바뀌어서 0이 된 부분을 구분하면 되는 것.

애초에 0인 spot을 다른 Array에 -1 값으로 넣고, -1인 spot은 switchToZero 메소드를 타면 끝.