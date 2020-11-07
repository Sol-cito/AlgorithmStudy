## Leetcode - Longest Increasing Subsequence [Medium]

Given an unsorted array of integers, find the length of longest increasing subsequence.

**Example:**

```
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
```

**Note:**

- There may be more than one LIS combination, it is only necessary for you to return the length.
- Your algorithm should run in O(*n^2*) complexity.

**Follow up:** Could you improve it to O(*n* log *n*) time complexity?

Link : https://leetcode.com/problems/longest-increasing-subsequence/



---

#### My solution (Java) - O(N^2)

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int answer = 0;
        for (int i = 0; i < nums.length; i++) {
            int last = nums[i];
            int com = nums[i];
            int cnt = 1;
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] > com) {
                    last = com;
                    com = nums[j];
                    cnt++;
                } else if (nums[j] > last) {
                    last = com;
                    com = nums[j];
                }
            }
            answer = Math.max(answer, cnt);
        }
        return answer;
    }
}
```

---

#### My logic & Feedback

O(N^2) 문제풀이의 관건은, 선형 탐색 도중 자신보다 작은 값을 만났을 때 그 값을 skip하고 다음 차례로 계속 탐색을 하는 것이다.

자신 바로 직전의 수를 변수에 저장해두고 비교하면 쉽게 풀린다.

즉,

```
[1,2,5,3,7]
```

위 경우, 5 > 3 이지만 2 < 3 이므로 탐색을 계속 해나가면 된다.

이 풀이방법이 가장 간단한 O(N^2) 풀이법인것 같은데, 

Follow Up 에서 말했던 O(NlogN) 로는 어떻게 풀이할까?

탐색이고, ascending order을 찾아나간다는 점에서 이분탐색일 거 같긴 한데..

다른사람들도 마찬가지로 이분탐색을 이용해 풀이한 것을 보았다. 

어쨌든 ascending order를 찾으면 되니까, O(N)으로 각 element를 시작점으로 하여 그 오른편에 있는 elements들에서

ascending order를 찾아나가는 풀이법 같다(코드로 직접 짜보자).

그런데 또 어떤 사람들은 **TreeSet**이라는 걸 썼는데..이건 처음보는 자료구조라 뭔지 모르겠다.

조금 파봐야겠다.



