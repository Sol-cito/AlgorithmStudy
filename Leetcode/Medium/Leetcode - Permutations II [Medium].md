## Leetcode - Permutations II [Medium]

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

**Example:**

```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```



Link : https://leetcode.com/problems/permutations-ii/



---



#### My solution (Java)

```java
class Solution {
    List<List<Integer>> resultList = new LinkedList<>();

    public List<List<Integer>> permuteUnique(int[] nums) {
       recursion(nums, new LinkedList<>(), new int[nums.length]);
        return resultList;
    }

    public void recursion(int[] nums, LinkedList<Integer> list, int[] indexArr) {
        if (list.size() == nums.length) {
            resultList.add(list);
            return;
        }
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (indexArr[i] == 0 && !set.contains(nums[i])) {
                list.add(nums[i]);
                int[] newIndexArr = indexArr.clone();
                newIndexArr[i] = 1;
                recursion(nums, new LinkedList<>(list), newIndexArr);
                list.removeLast();
                set.add(nums[i]);
            }
        }
    }
}


```

---



#### My logic & Feedback

Permutations 문제와 비슷하지만, 중복된 element가 있다는 점이 다르다.

set을 이용, 중복된 element가 있을 경우 재귀를 한번만 돌도록 수정해주면 된다.