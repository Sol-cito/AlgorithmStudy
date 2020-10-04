## Leetcode - Rectangle Area [Medium]

\223. Rectangle Area

Medium

450785Add to ListShare

Find the total area covered by two **rectilinear** rectangles in a **2D** plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

![Rectangle Area](https://assets.leetcode.com/uploads/2018/10/22/rectangle_area.png)

**Example:**

```
Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
```

**Note:**

Assume that the total area is never beyond the maximum possible value of **int**.



Link : https://leetcode.com/problems/rectangle-area/

---



#### My solution (Java)

```java
class Solution {
     public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int answer = Math.abs(A - C) * Math.abs(B - D) + Math.abs(E - G) * Math.abs(F - H);
        int startX = Math.max(A, E);
        int endX = Math.min(C, G);
        int startY = Math.max(B, F);
        int endY = Math.min(D, H);
        if (startX < endX && startY < endY) {
            answer -= (endX - startX) * (endY - startY);
        }
        return answer;
    }
}
```

---



#### My logic & Feedback

그냥 수학문제다...

두 사각형의 넓이를 더한 후(answer), 겹치는 부분이 있으면 겹치는 부분만큼 빼주면 끝.

겹치는 부분의 조건은 (startX < endX && startY < endY) 이므로 겹칠 때만 빼주면 된다.