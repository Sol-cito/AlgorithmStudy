## Leetcode - Remove Duplicates from Sorted Array [Easy]

Given a sorted array *nums*, remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each element appears only *once* and returns the new length.

Do not allocate extra space for another array, you must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

**Clarification:**

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by **reference**, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:

```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

 

**Example 1:**

```
Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
```

**Example 2:**

```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
```

 

**Constraints:**

- `0 <= nums.length <= 3 * 104`
- `-104 <= nums[i] <= 104`
- `nums` is sorted in ascending order.

Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/



---



#### My solution (Python)

```java
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums: return 0
        num = nums[0]
        pointer1 = pointer2 = 1
        while (pointer1 < len(nums)):
            if (num == nums[pointer1]):
                pointer1 += 1
            else:
                nums[pointer2] = nums[pointer1]
                num = nums[pointer1]
                pointer2 += 1
        return pointer2
```

---



#### My logic & Feedback

파이썬으로 푼 흥미로운 문제! 요즘 파이썬에 익숙해지기 위해 Easy문제는 Python으로 풀고있다.

파이썬 문법은 정말 직관적이고, 프로그래밍 언어라기보다는 영어문장의 느낌이 강하다.

그래서 Java보다 훨씬 유연하게 느껴진다.

풀이는 쉽다. sorted array이기 때문에 O(N)으로 탐색을 하는데, 

값을 가리킬 pointer 2개를 설정하여 값을 비교해나가면 된다.

전형적인 **two pointer** 문제!