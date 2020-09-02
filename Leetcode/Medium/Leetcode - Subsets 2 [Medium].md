## Leetcode - Subsets 2 [Medium]

Given a collection of integers that might contain duplicates, ***nums\***, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:**

```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

Link : https://leetcode.com/problems/subsets-ii/



---



#### My solution (Java)

```java
class Solution {
    List<List<Integer>> returnList = new LinkedList<>();

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i <= nums.length; i++) {
            recursion(nums, 0, new LinkedList<Integer>(), i);
        }
        return returnList;
    }

    public void recursion(int[] nums, int startPoint, LinkedList<Integer> linkedList, int size) {
        if (linkedList.size() == size) {
            returnList.add(linkedList);
            return;
        }
        int lastInt = 0;
        for (int i = startPoint; i < nums.length; i++) {
            if(i == startPoint || nums[i] != lastInt){ 
                linkedList.add(nums[i]);
                recursion(nums, i + 1, new LinkedList<>(linkedList), size);
                linkedList.removeLast();
                lastInt = nums[i];
            }
        }
    }
}        
   
```

---



#### My logic & Feedback

재귀로 접근하는 것은 Subsets 문제와 똑같은데, 중복 제거를 해야된다는 점이 다르다.

재귀 method에서 for문을 돌 때, lastInt 라는 integer를 설정하여 다음번 for문의 대상 원소가 이전 숫자와 같다면 재귀를 돌지 않으면 간단히 해결된다.