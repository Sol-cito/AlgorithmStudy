## Leetcode - Spiral Matrix [Medium]

Given a matrix of *m* x *n* elements (*m* rows, *n* columns), return all elements of the matrix in spiral order.

**Example 1:**

```
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**

```
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```



Link : https://leetcode.com/problems/spiral-matrix/

---



#### My solution (Java)

```java
class Solution {
     public List<Integer> spiralOrder(int[][] matrix) {
        ArrayList<Integer> result = new ArrayList<>();
        if (matrix.length == 0 || matrix[0].length == 0) {
            return result;
        }
        int leftWall = 0;
        int rightWall = matrix[0].length;
        int ceiling = 0;
        int bottom = matrix.length;

        while (bottom > ceiling && leftWall < rightWall) {
            rotate(matrix, leftWall, rightWall, ceiling, bottom, result, matrix.length * matrix[0].length);
            leftWall++;
            rightWall--;
            ceiling++;
            bottom--;
        }
        return result;
    }

    public void rotate(int[][] matrix, int leftWall, int rightWall, int ceiling, int bottom, ArrayList<Integer> result, int size) {
        for (int i = leftWall; i <= rightWall - 1; i++) {
            result.add(matrix[ceiling][i]);
            if (result.size() >= size) {
                return;
            }
        }
        for (int i = ceiling + 1; i < bottom - 1; i++) {
            result.add(matrix[i][rightWall - 1]);
            if (result.size() >= size) {
                return;
            }
        }
        for (int i = rightWall - 1; i >= leftWall + 1; i--) {
            result.add(matrix[bottom - 1][i]);
            if (result.size() >= size) {
                return;
            }
        }
        for (int i = bottom - 1; i >= ceiling + 1; i--) {
            result.add(matrix[i][leftWall]);
            if (result.size() >= size) {
                return;
            }
        }
    }
}
```

---



#### My logic & Feedback

풀긴 하였는데 마음에 들지는 않는다. 코드가 좀 더럽다.

그냥 충실히 상하좌우 탐색해가며 구현하는 방법밖에 없는듯 한데...

주어진 Matrix가 정사각형이 아니기 때문에 마지막에 중복되는 부분이 존재한다. 그래서

```
if (result.size() >= size) {
	return;
}
```

위 코드를 넣을 수 밖에 없었는데, 

저렇게 하면 코드량이 엄청 늘어나기때문에 비효율적이다. 코드 구성을 조금 달리하면 훨씬 깔끔할텐데...