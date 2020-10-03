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

#### My solution (Java) - Bruth Force (62ms / 42.3 MB)

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



---

#### My solution (Java) - DP (4ms / 42.3 MB)

위 말대로 DP로 어떻게 풀 수 있을지 고민하다 완성한 코드!

```
class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix.length == 0) {
            return 0;
        }
        int[] dpArr = new int[matrix[0].length];
        int answer = 0;

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == '0') {
                    dpArr[j] = 0;
                } else {
                    dpArr[j]++;
                }
            }
            answer = Math.max(answer, renewDPArr(dpArr));
        }
        return answer * answer;
    }

    public int renewDPArr(int[] dpArr) {
        int maxArea = 0;
        for (int i = 0; i < sum.length; i++) {
            int cnt = 0;
            int rangeLimit = i + sum[i];
            int targetNum = sum[i];
            for (int j = i; j < rangeLimit && j < sum.length; j++) {
                if (sum[j] < targetNum) {
                    rangeLimit -= (targetNum - sum[j]);
                    targetNum = sum[j];
                }
                if (j < rangeLimit) {
                    cnt++;
                }
            }
            maxArea = Math.max(maxArea, cnt);
        }
        return maxArea;
    }
}
```

---

#### My logic & Feedback

결국 DP 방식으로 풀었다!

풀이 방법은 이렇다.

먼저 int[] dpArr 라는 1차원 배열을 만드는데, 이 배열은 matrix 의 로우를 한 줄씩 탐색할 때마다 갱신된다. 어떻게?

dpArr = { 1, 0, 1, 1, 1} 이고 matrix의 다음 로우가 {1, 1, 1, 0, 0} 이라면, dpArr는 {2, 1, 2, 0, 0} 이 되는 셈이다.

이 때 dpArr의 element가 의미하는 것은 **'위에서 내려온 연속된 숫자와 현재 숫자의 합'**이다.

즉 dpArr의 element 값이 3 이라는 것은 두 줄 위에서부터 1이 세 번 연속해있다는 것이며,

element의 값이 0 이라는 것은 해당 row 위쪽에 어떤 값들이 있는지는 상관없이 위쪽 row의 값들과는 연속되지 않아 단절되어있다는 것이다.

dpArr를 한 번 갱신할 때마다 renewDPArr 메소드를 타며 maxArea를 찾는다.

dpArr를 linear하게 탐색하면서 가장 긴 범위를 찾는 것이다.

DP로 푼 결과, 완전탐색에 비해 추가 메모리 자원의 낭비 없이 성능이 **15배**가 향상되는(!!) 결과를 얻었다.

DP로 풀이방법을 생각해내는건 어렵지만, 그만큼 성능 향상이 강력하므로 idea를 떠올리는 데 능숙해져야 한다.