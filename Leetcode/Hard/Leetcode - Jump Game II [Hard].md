## Leetcode - Jump Game II [Hard]

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

**Example:**

```
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Note:**

You can assume that you can always reach the last index.



Link : https://leetcode.com/problems/jump-game-ii/

---



#### My solution (Java)

```java
class Solution {
    public int jump(int[] nums) {
        if (nums.length < 2) return 0;
        int startIndex = 0;
        int maxRange = nums[startIndex];
        int answer = 1;
        while (maxRange < nums.length - 1) {
            int newMaxRange = 0;
            for (int i = startIndex; i <= maxRange && i < nums.length; i++) {
                newMaxRange = Math.max(newMaxRange, i + nums[i]);
            }
            startIndex = maxRange + 1;
            maxRange = newMaxRange;
            answer++;
        }
        return answer;
    }
}
```

---

#### My logic & Feedback

My first idea was using BFS to reach the last index as fast as possible.

But soon I realized each attempt had overlapped index range, so I pivoted to DP approach.

The whole point of this problem is to renew the farthest index so that we can figure out if the next jump can reach the last index of not.

Through loop, the start index and the farthest index can be renewed each time we search a certain range from start index to the maxRange.

Return answer - the number of attempt - when maxRange reaches or exceeds the last index of the array.



