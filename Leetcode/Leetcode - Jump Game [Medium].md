## Leetcode - Jump Game [Medium]

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

 

**Constraints:**

- `1 <= nums.length <= 3 * 10^4`
- `0 <= nums[i][j] <= 10^5`

Link : https://leetcode.com/problems/jump-game/



---



#### My solution (Java)

```java
class Solution {
   boolean answer = false;

    public boolean canJump(int[] nums) {
        recursion(nums, 0, 0);
        return answer;
    }

    public void recursion(int[] nums, int pointer, int max) {
        if (max >= nums.length - 1) {
            answer = true;
            return;
        }
        for (int i = pointer + 1; i <= pointer + nums[pointer]; i++) {
            if (i < nums.length && i + nums[i] > max && !answer) {
                recursion(nums, i, i + nums[i]);
            }
        }
    }
}

```

---



#### My logic & Feedback

재귀로 접근한 문제. 

재귀를 돌면서 각각의 차례에서의 가장 넓은 범위(max)를 구하여, 끝까지 닿으면 return하는 방식이다.

재귀를 돌기 때문에 성능에서는 사실 상당히 떨어진다.

다른 답변을 보니 끝 지점에서부터 거꾸로 가는 DP방식을 썼던데, 훨씬 빠르고 직관적이라 그 방법이 훨씬 더 나은 것 같다.