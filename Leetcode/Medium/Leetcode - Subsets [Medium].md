## Leetcode - Search a 2D Matrix [Medium]

Given a set of **distinct** integers, *nums*, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:**

```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

Link : https://leetcode.com/problems/subsets/



---



#### My solution (Java)

```java
class Solution {
       List<List<Integer>> result = new LinkedList<>();

    public List<List<Integer>> subsets(int[] nums) {
        for (int i = 0; i <= nums.length; i++) {
            LinkedList<Integer> linkedList = new LinkedList<>();
            recursion(nums, i, linkedList, 0);
        }
        return result;
    }

    public void recursion(int[] nums, int size, LinkedList<Integer> linkedList, int startIndex) {
        if (linkedList.size() == size) {
            result.add(linkedList);
            return;
        }
        for (int i = startIndex; i < nums.length; i++) {
            linkedList.add(nums[i]);
            recursion(nums, size, new LinkedList<>(linkedList), i + 1);
            linkedList.removeLast();
        }
    }
}
```

---



#### My logic & Feedback

이 문제는 솔직히 난이도가 Easy같은데..왜 Medium에 있담..

가능한 조합을 재귀로 구해서 반환하면 끝!

