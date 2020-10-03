## Leetcode - Dungeon Game [Hard]

Given a set of *non-overlapping* intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

**Example 1:**

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2:**

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.출처 

Link: https://leetcode.com/problems/insert-interval/



---



#### My solution (Java)

```java
class Solution {
   public int calculateMinimumHP(int[][] dungeon) {
        int[][] valueArr = new int[dungeon.length][dungeon[0].length];
        int lastNodeValue = dungeon[dungeon.length - 1][dungeon[0].length - 1];
        if (lastNodeValue >= 0) {
            valueArr[dungeon.length - 1][dungeon[0].length - 1] = 0;
        } else {
            valueArr[dungeon.length - 1][dungeon[0].length - 1] = -lastNodeValue;
        }

        for (int i = dungeon.length - 1; i >= 0; i--) {
            for (int j = dungeon[0].length - 1; j >= 0; j--) {
                if (i < dungeon.length - 1 && j == dungeon[0].length - 1) {
                    fromBottom(valueArr, dungeon, i, j);
                } else if (i == dungeon.length - 1 && j < dungeon[0].length - 1) {
                    fromRight(valueArr, dungeon, i, j);
                } else if (i < dungeon.length - 1 && j < dungeon[0].length - 1) {
                    if (valueArr[i + 1][j] < valueArr[i][j + 1]) {
                        fromBottom(valueArr, dungeon, i, j);
                    } else {
                        fromRight(valueArr, dungeon, i, j);
                    }
                }
            }
        }
        return valueArr[0][0] + 1;
    }

    public void fromBottom(int[][] valueArr, int[][] dungeon, int i, int j) {
        if (dungeon[i][j] >= valueArr[i + 1][j]) {
            valueArr[i][j] = 0;
        } else {
            valueArr[i][j] = valueArr[i + 1][j] - dungeon[i][j];
        }
    }

    public void fromRight(int[][] valueArr, int[][] dungeon, int i, int j) {
        if (dungeon[i][j] >= valueArr[i][j + 1]) {
            valueArr[i][j] = 0;
        } else {
            valueArr[i][j] = valueArr[i][j + 1] - dungeon[i][j];
        }
    }
}
```

---

#### My logic & Feedback

I found this problem quite interesting (the description of it is even so cool because everyone knows this type of game).

At first glance, it came to me as a simple DFS problem, but hard problem never disappoints me. Time limit excess took place.

Considering the knight only goes right and down, I approached it by Dynamic Programming, but in reverse order (From the last spot to the starting point).

Going backwards, each element of newly created array 'valueArr' is renewed by referring to it's 'underneath grid' and 'right grid', which were the previous steps of it.

If previous value is negative, it means **the knight had to have one more HP than previous value when he was on the previous spot**. 

If positive, it means **the knight's HP could be the amount less than the positive value **.

Following those rules, return the value of first spot.



