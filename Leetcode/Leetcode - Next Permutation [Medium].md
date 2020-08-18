## Leetcode - Next Permutation [Medium].md

Implement **next permutation**, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be **[in-place](http://en.wikipedia.org/wiki/In-place_algorithm)** and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

```
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```

Link : https://leetcode.com/problems/next-permutation/



---



#### My solution (Java)

```java
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {class Solution {
 public void nextPermutation(int[] nums) {
        int targetIndex = nums.length - 2;
        while (targetIndex < nums.length && targetIndex >= 0) {
            for (int i = nums.length - 1; i >= targetIndex; i--) {
                if (nums[i] > nums[targetIndex]) {
                    int val = nums[targetIndex];
                    nums[targetIndex] = nums[i];
                    nums[i] = val;
                    PriorityQueue<Integer> pq = new PriorityQueue<>();
                    for (int j = targetIndex + 1; j < nums.length; j++) {
                        pq.add(nums[j]);
                    }
                    targetIndex++;
                    while (!pq.isEmpty()) {
                        nums[targetIndex] = pq.poll();
                        targetIndex++;
                    }
                    return;
                }
            }
            targetIndex--;
        }
        Arrays.sort(nums);
    }
}
```

---



#### My logic & Feedback

어떻게 하면 숫자를 움직여서 '한 단계 큰 수'를 만들 수 있을까를 고민하는 문제.

방법은, 1의 자리수부터 자신과 가장 가까운 숫자를 보고, 자신보다 크면 그 둘을 swap해준 뒤,

swap한 자리(위 코드에서 targetIndex) 아래 숫자들을 오름차순 정렬해주면 된다.

오름차순 정렬을 PriorityQueue를 써서 간단히 해결하였고,

만약 바꿀 수가 하나도 없는 경우는 Arrays.sort 내장함수를 써서 간단히 해결하였다.

