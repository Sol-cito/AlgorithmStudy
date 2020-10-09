## Leetcode - Search a 2D Matrix II [Medium]

- Write an efficient algorithm that searches for a value in an *m* x *n* matrix. This matrix has the following properties:

  - Integers in each row are sorted in ascending from left to right.
  - Integers in each column are sorted in ascending from top to bottom.

  **Example:**

  Consider the following matrix:

  ```
  [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
  ]
  ```

  Given target = `5`, return `true`.

  Given target = `20`, return `false`.

Link : https://leetcode.com/problems/search-a-2d-matrix-ii/



---



#### My solution (Java) - 11ms , 44.6MB

```java
class Solution {
     public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }
        int x = matrix.length - 1;
        for (int i = 0; i < matrix.length - 1; i++) {
            if (matrix[i][0] <= target && target < matrix[i + 1][0]) {
                x = i;
                break;
            }
        }
        int y = matrix[0].length - 1;
        for (int i = 0; i < matrix[0].length - 1; i++) {
            if (matrix[0][i] <= target && target < matrix[0][i + 1]) {
                y = i;
                break;
            }
        }
        for (int i = x; i >= 0; i--) {
            for (int j = y; j >= 0; j--) {
                if (matrix[i][j] == target) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

---



#### My logic & Feedback

문제는 매우 쉽다. 문제가 쉬워서 별 생각 안하고 떠오르는대로 구현하고 바로 풀었다.

그런데 생각보다 성능이 구렸고, Discussion 게시판에서 추천을 많이 받은 답을 찾아봤는데...

Like를 가장 많이 받은 Solution이 진짜 기가막혔다..

그것은 바로, **BST (Binary Search Tree)**를 이용하는 것!

해당 모범답변의 solution을 카피해서 구현한 결과는 아래와 같다 (4ms, 44.4MB)

```
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }
        int x = 0, y = matrix[0].length - 1;
        while (x < matrix.length && x >= 0 && y < matrix[0].length && y >= 0) {
            if (matrix[x][y] < target) {
                x++;
            } else if (matrix[x][y] > target) {
                y--;
            } else {
                return true;
            }
        }
        return false;
    }
}
```

코드가 너무나 Neat하고 아이디어도 기가막힌다.

Point는, 주어진 배열을 '2진 트리'로 본다는 것이다. 

```
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
```

위 2차원 배열은 오른쪽, 아래로 갈 수록 값이 증가한다.

오른쪽을 Parent Node로, 왼쪽을 Child Node로 본다면 BST에 온전히 부합한다.

BST는 탐색 속도가 LogN으로, 내가 최초로 짠 코드의 탐색 속도가 O(N)인 것에 비하면 속도가 훨씬 빠르다.

배열을 보고 트리를 생각해내다니..정말 한 수 배웠다.

이 문제와 비슷한 문제로, 프로그래머스의 **길찾기 게임** 이 있는데(https://programmers.co.kr/learn/challenges?selected_part_id=12286)

이 문제도 풀어서 Github에 올려놓았다.