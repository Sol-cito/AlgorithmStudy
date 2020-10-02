## Leetcode - Summary Ranges [Medium]

You are given a **sorted unique** integer array `nums`.

Return *the **smallest sorted** list of ranges that **cover all the numbers in the array exactly***. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:

- `"a->b"` if `a != b`
- `"a"` if `a == b`

 

**Example 1:**

```
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

**Example 2:**

```
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

**Example 3:**

```
Input: nums = []
Output: []
```

**Example 4:**

```
Input: nums = [-1]
Output: ["-1"]
```

**Example 5:**

```
Input: nums = [0]
Output: ["0"]
```

 

**Constraints:**

- `0 <= nums.length <= 20`
- `-231 <= nums[i] <= 231 - 1`
- All the values of `nums` are **unique**.

Link : https://leetcode.com/problems/summary-ranges/



---



#### My solution (Java)

```java
class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> answer = new ArrayList<>();
        if(nums.length == 0){
            return answer;
        }
        int pointerNum = nums[0];
        int prevNum = nums[0];
        int cnt = 0;
        StringBuilder sb = new StringBuilder("" + nums[0]);

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == pointerNum + 1) {
                pointerNum++;
                cnt++;
            } else if (nums[i] != pointerNum + 1) {
                if (cnt == 0) {
                    answer.add(sb.toString());
                } else {
                    answer.add(sb.append("->" + prevNum).toString());
                }
                sb = new StringBuilder("" + nums[i]);
                pointerNum = nums[i];
                cnt = 0;
            }
            prevNum = nums[i];
        }
        if (cnt == 0) {
            answer.add(sb.toString());
        } else {
            answer.add(sb.append("->" + prevNum).toString());
        }
        return answer;
    }
}
```

---



#### My logic & Feedback

쉬운 문제라 한번에 풀 수 있었다 (그래서 코드 정리도 안했..).

prevNum (이전 값)과 pointerNum(현재값)을 잘 저장해두었다가 값의 범위가 바뀌는 시점에서 StringBuilder로 만들어놓은

Stirng을 list에 담으면 끝.