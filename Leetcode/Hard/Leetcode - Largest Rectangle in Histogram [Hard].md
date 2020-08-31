## Leetcode - Largest Rectangle in Histogram [Hard]

Given *n* non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 

![img](https://assets.leetcode.com/uploads/2018/10/12/histogram.png)
Above is a histogram where width of each bar is 1, given height = `[2,1,5,6,2,3]`.

 

![img](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)
The largest rectangle is shown in the shaded area, which has area = `10` unit.

Link : https://leetcode.com/problems/largest-rectangle-in-histogram/



---



#### My solution (Java)

```java
class Solution {
   public int largestRectangleArea(int[] heights) {
        int answer = 0;
        for (int i = 0; i < heights.length; i++) {
            int leftPointer = i;
            while (leftPointer > 0 && heights[leftPointer - 1] >= heights[i]) {
                leftPointer--;
            }
            int rightPointer = i;
            while (rightPointer < heights.length - 1 && heights[rightPointer + 1] >= heights[i]) {
                rightPointer++;
            }
            answer = Math.max(answer, (rightPointer - leftPointer + 1) * heights[i]);
        }
        return answer;
    }
}
```

---



#### My logic & Feedback

I think this problem do not deserve to be a Hard level problem (Medium is where it should be).

Main idea is, to search all the bars and to verify all the other histogram bars on both side to see if the rest of bars could high enough to satisfy the selected bar's height.

For instance, if I select the bar number 5 (height is two), see other bars on the left and right and check if they are lower than the bar. 

If so, stop measuring and return the calculation.

Finally return the maximum value of each calculation.

