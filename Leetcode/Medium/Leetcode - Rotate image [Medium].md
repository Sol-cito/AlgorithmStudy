## Leetcode - Rotate image [Medium]

You are given an *n* x *n* 2D `matrix` representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm), which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

**Example 3:**

```
Input: matrix = [[1]]
Output: [[1]]
```

**Example 4:**

```
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
```

 

**Constraints:**

- `matrix.length == n`
- `matrix[i].length == n`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

Link : https://leetcode.com/problems/rotate-image/

---



#### My solution (Java)

```java
class Solution {
   public void rotate(int[][] matrix) {
        int leng = matrix.length - 1;
        for (int i = 0; i < matrix.length / 2; i++) {
            int[] pointer = {i, i};
            for (int j = 0; j < leng; j++) {
                searchAndSwap(pointer, i, matrix.length - 1 - i, matrix, matrix[pointer[0]][pointer[1]], 0);
                pointer[1]++;
            }
            leng -= 2;
        }
    }

    public void searchAndSwap(int[] pointer, int smallNum, int largeNum, int[][] matrix, int value, int count) {
        if (count == 4) {
            return;
        }
        int cnt = 0;
        int length = largeNum - smallNum;
        while (cnt < length) {
            if (pointer[0] == smallNum && pointer[1] < largeNum) {
                pointer[1]++;
            } else if (pointer[1] == largeNum && pointer[0] < largeNum) {
                pointer[0]++;
            } else if (pointer[0] == largeNum && pointer[1] > smallNum) {
                pointer[1]--;
            } else if (pointer[1] == smallNum && pointer[0] > smallNum) {
                pointer[0]--;
            }
            cnt++;
        }
        int nextValue = matrix[pointer[0]][pointer[1]];
        matrix[pointer[0]][pointer[1]] = value;
        searchAndSwap(pointer, smallNum, largeNum, matrix, nextValue, count + 1);
    }
}
```

---



#### My logic & Feedback

이 문제에 다른 꼼수가 있는지는 모르겠고...그냥 착실히 하나하나 구현해서 풀었다(그래서 중간중간에 에러도 많이나서 굉장히 짜증남).

그래서인지 속도는 100%, 메모리는 약 90% beat rate가 나왔다.

사실 이런 빡구현 문제는 말 그대로 빡구현하는게 가장 성능이 좋긴 한데...그 과정이 힘들어서 문제지..