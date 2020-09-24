## Leetcode - 3sum [Medium]

Given an array `nums` of *n* integers, are there elements *a*, *b*, *c* in `nums` such that *a* + *b* + *c* = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

**Example 1:**

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2:**

```
Input: nums = []
Output: []
```

**Example 3:**

```
Input: nums = [0]
Output: []
```

 

**Constraints:**

- `0 <= nums.length <= 3000`
- `-105 <= nums[i] <= 105`

Link : https://leetcode.com/problems/3sum/



---



#### My solution (Java)

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        if (nums.length == 0) {
            return answer;
        }
        HashMap<Integer, Integer> map = new HashMap<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        int prev_i = nums[0];
        for (int i = 0; i < nums.length; i++) {
            if (i == 0 || nums[i] != prev_i) {
                int prev_j = nums[i];
                for (int j = i + 1; j < nums.length; j++) {
                    if (j == i + 1 || nums[j] != prev_j) {
                        int negativeSum = -(nums[i] + nums[j]);
                        if (map.get(negativeSum) != null && map.get(negativeSum) > j) {
                            List<Integer> list = new ArrayList<>();
                            list.add(nums[i]);
                            list.add(nums[j]);
                            list.add(negativeSum);
                            answer.add(list);
                        }
                    }
                    prev_j = nums[j];
                }
                prev_i = nums[i];
            }
        }
        return answer;
    }
}
```

---



#### My logic & Feedback

이 악마의 문제.............

한 달 전에 문제풀이를 시도하다가 10번은 넘게 submission fail 하였다...현재 내 Leetcode 오답률을 높인 주범 중 하나.

딱 보기에는 쉬워보이는데, 무턱대고 for문 3번을 돌리다간 Time limit exceed가 난다.

그리고 중복제거, 0의 유무 등 생각해야 할 조건이 까다롭기 때문에 단순히 접근해서는 문제가 풀리지 않았다.

그리고 이 문제가 풀린 순간은 언제나 그랬듯, 시간이 한참 지나고 난 후 다시 문제를 보며 곰곰히 생각하던 순간이었다.



알고리즘 문제 중 상당히 유명한 문제가 있다.

int[] arr 가 있을 때, 두 수를 더해서 k가 될 수 있는지 어떻게 알 수 있을까?

단순히 생각하면 정렬 후 for문을 2번 돌려서 k가 되는 경우를 검사해보면 되고, 이 때의 시간복잡도는 O(N^2)이 된다.

그런데 만약 HashMap을 이용하면, 시간복잡도를 O(N)으로 줄일 수 있다. 어떻게?

우선 for문을 한번 돌면서 Map에 각 element를 담는다.

그리고 다시 한 번 for문을 돌면서 map.get(k - arr[i]) 가 null이 아닌지 보면 된다!

HashMap은 시간복잡도가 O(1)이므로 가능한 방법이다.



이를 응용하여, 위의 3sum 문제를 풀었다.

정렬 후, 두 elements를 더한 값이 map에 담겨있는지 검사하고, 

만약 map에 담겨있으면서 **두 elements 중 index가 더 큰 놈보다 map에 담긴 element의 index가 클 경우**가 정답.

index가 커야하는 이유는, 그래야만 중복을 제거할 수 있기 때문이다.

만약 int[]  = {-1, 0, 1} 이 있을 때 index를 고려하지 않는다면, 두 element가 {-1, 0} 일 때와 {0, -1}일때의 최종 결과값이 중복될 것이므로..