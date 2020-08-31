## Leetcode - Search a 2D Matrix [Medium]

Write an efficient algorithm that searches for a value in an *m* x *n* matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

**Example 1:**

```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
```

**Example 2:**

```
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
```

Link : https://leetcode.com/problems/search-a-2d-matrix/



---



#### My solution (Java)

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }
        for (int i = 0; i < matrix.length; i++) {
            if (matrix[i][0] <= target && matrix[i][matrix[i].length - 1] >= target) {
                return binarySearch(matrix[i], target);
            }
        }
        return false;
    }

    public boolean binarySearch(int[] matrixRow, int target) {
        int left = 0;
        int right = matrixRow.length - 1;
        int pointer = (left + right) / 2;
        while (left <= right) {
            if (matrixRow[pointer] == target) {
                return true;
            }
            if (matrixRow[pointer] < target) {
                left = pointer + 1;
            } else {
                right = pointer - 1;
            }
            pointer = (left + right) / 2;
        }
        return false;
    }
}
```

---



#### My logic & Feedback

1차원적으로 완전탐색으로 풀 수도 있으나,

한 row의 처음과 끝 수가 target 범위 안에 있으면, 해당 row를 (sorted) 이분탐색하는 것이 가장 효율적이라 생각했다.

이분탐색을 오랜만에 구현했는데, left <= right 조건으로 while문 탈출을 하지 않고 pointer가 담은 이전 번 value를 가지고 비교를 했더니 모든 케이스를 탐색하지 못하는 약점이 있었다.

left와 right가 교차되는 시점이 탈출조건임을 반드시 기억해야겠다.

