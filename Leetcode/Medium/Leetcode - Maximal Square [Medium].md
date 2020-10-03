## Leetcode - Maximal Square [Medium]

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

**Example:**

```
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```

Link : https://leetcode.com/problems/maximal-square/



---



#### My solution (Java)

```java
class Solution {
   public int maximalSquare(char[][] matrix) {
        if(matrix.length == 0){
            return 0;
        }
        int length = Math.min(matrix[0].length, matrix.length);
        while (length > 0) {
            for (int i = 0; i <= matrix.length - length; i++) {
                for (int j = 0; j <= matrix[0].length - length; j++) {
                    if (findSquare(i, j, matrix, length)) {
                        return length * length;
                    }
                }
            }
            length--;
        }
        return 0;
    }

    public boolean findSquare(int x, int y, char[][] matrix, int length) {
        for (int i = x; i < x + length; i++) {
            for (int j = y; j < y + length; j++) {
                if (matrix[i][j] == '0') {
                    return false;
                }
            }
        }
        return true;
    }
}
```

---



#### My logic & Feedback

'정사각형'을 완전탐색으로 찾으면 되는 쉬운 문제다.

가장 큰 넓이를 찾는 것이기에, 주어진 gird의 가로, 세로 중 더 작은 것을 최대 변으로, 

변의 길이를 1씩 줄여나가면서 정사각형이 있는지를 탐색하면 된다.

그런데 이 방식은 사실 완전탐색이라...효율성이 떨어진다.

DP를 활용한 방법이 무조건 있을텐데, 어떻게 DP로 풀지 조금 고민해봐야겠다.