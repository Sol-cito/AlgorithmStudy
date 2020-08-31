## Leetcode - Permutations [Medium]

- Given a collection of **distinct** integers, return all possible permutations.

  **Example:**

  ```
  Input: [1,2,3]
  Output:
  [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
  ]
  ```

Link : https://leetcode.com/problems/permutations/



---



#### My solution (Java)

```java
class Solution {
  List<List<Integer>> resultList = new LinkedList<>();

    public List<List<Integer>> permute(int[] nums) {
        recursion(nums, new LinkedList<>(), new int[nums.length]);
        return resultList;
    }

    public void recursion(int[] nums, LinkedList<Integer> list, int[] indexArr) {
        if (list.size() == nums.length) {
            resultList.add(list);
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (indexArr[i] == 0) {
                list.add(nums[i]);
                int[] newIndexArr = indexArr.clone();
                newIndexArr[i] = 1;
                recursion(nums, new LinkedList<>(list), newIndexArr);
                list.removeLast();
            }
        }
    }
}

```

---



#### My logic & Feedback

Permutation 이란 순열이라는 뜻이므로, 재귀로 순열을 구해주면 된다.

여러가지 방법이 있겠지만, 나는 LinkedList와 IndexArray를 통해 노드를 추가함과 동시에 index를 저장하여 중복된 index가 없도록 구현하였다.