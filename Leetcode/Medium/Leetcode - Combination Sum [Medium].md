## Leetcode - Combination Sum [Medium]

Given a **set** of candidate numbers (`candidates`) **(without duplicates)** and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

The **same** repeated number may be chosen from `candidates` unlimited number of times.

**Note:**

- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

**Example 2:**

```
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

Link : https://leetcode.com/problems/combination-sum/



---



#### My solution (Java)

```java
class Solution {
 List<List<Integer>> answer = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        recursion(candidates, target, 0, new ArrayList<>(), 0);
        return answer;
    }

    public void recursion(int[] candidates, int target, int sum, ArrayList<Integer> list, int startIndex) {
        if (sum >= target) {
            if (sum == target) {
                answer.add(list);
            }
            return;
        }
        for (int i = startIndex; i < candidates.length; i++) {
            ArrayList<Integer> copied = arrayCopy(list);
            copied.add(candidates[i]);
            recursion(candidates, target, sum + candidates[i], copied, i);
        }
    }

    public ArrayList<Integer> arrayCopy(ArrayList<Integer> list) {
        ArrayList<Integer> copied = new ArrayList<>();
        for (int each : list) {
            copied.add(each);
        }
        return copied;
    }
}
```

---



#### My logic & Feedback

재귀로 조합의 경우의 수를 구하면 되는 아주 쉬운 문제다.

그런데 다른 답을 보니 DP로 풀었던데...DP로는 어떻게 풀지 고민해봐야겠다.

또한, ArrayList를 복사하는 메소드를 나는 여태까지 따로 만들어왔었는데, new ArrayList<Integer>(old list) 와 같은 형식으로도 가능하다??

이것도 한번 파보아야겠다.