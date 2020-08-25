## Leetcode - Combination Sum II [Medium]

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:**

- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

**Example 2:**

```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

Link : https://leetcode.com/problems/combination-sum-ii/



---



#### My solution (Java)

```java
class Solution {
     List<List<Integer>> resultList = new ArrayList<>();

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        LinkedList<Integer> list = new LinkedList<>();
        recursion(candidates, target, 0, 0, list);
        return resultList;
    }

    public void recursion(int[] candidates, int target, int sum, int startIndex, LinkedList<Integer> list) {
        if (sum >= target) {
            if (sum == target) {
                resultList.add(list);
            }
            return;
        }
        int previousNum = -1;
        for (int i = startIndex; i < candidates.length; i++) {
            if (candidates[i] != previousNum) {
                list.add(candidates[i]);
                recursion(candidates, target, sum + candidates[i], i + 1, new LinkedList<>(list));
                previousNum = candidates[i];
                list.removeLast();
            }
        }
    }
}
```

---



#### My logic & Feedback

Combination Sum 1 과 유사한 방식으로 재귀로 풀었다.

그리고 다른 사람들의 답을 보면서 기막힌 방식을 하나 보고야 말았다.

나는 여태까지 ArrayList를 복사하면서 다음 재귀로 넘겼고, 그래서인지 복사 메소드를 무조건 하나 만들곤 했다.

그런데 답에서 요구하는것은 List<List<Integer>> 이므로, 결국 List를 구현한 객체를 반환하면 된다.

따라서 LinkedList를 반환해도 되고, LinkedList 또한 복사해야하는건 마찬가지지만 마지막 노드만 제거하고 반환하면 된다.

remove 함수가 ArrayList의 경우는 객체를 아예 새로 만드는 방식인데, LinkedList는 주소만 자르는 방식이라 더 빠르지 않을까?

한번 파봐야겠다.