## Leetcode - Merge Intervals [Medium]

Given a collection of intervals, merge all overlapping intervals.

**Example 1:**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2:**

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 

**Constraints:**

- `intervals[i][0] <= intervals[i][1]`



Link :https://leetcode.com/problems/merge-intervals/

---



#### My solution (Java)

```java
class Solution {
   public int[][] merge(int[][] intervals) {
        if (intervals.length == 0) {
            return intervals;
        }
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });

        int open = intervals[0][0];
        int close = intervals[0][1];
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] >= open && intervals[i][0] <= close && intervals[i][1] > close) {
                close = intervals[i][1];
            } else if (intervals[i][0] > close) {
                list.add(open);
                list.add(close);
                open = intervals[i][0];
                close = intervals[i][1];
            }
        }
        list.add(open);
        list.add(close);
        int[][] resultArr = new int[list.size() / 2][2];
        for (int i = 0; i < list.size(); i += 2) {
            resultArr[i / 2][0] = list.get(i);
            resultArr[i / 2][1] = list.get(i + 1);
        }
        return resultArr;
    }
}
```

---



#### My logic & Feedback

여러가지 풀이방법이 있겠지만, O(N)번의 탐색으로 값을 갱신해나가는 방법이 가장 빠르고 효율적이라 생각했다.

a ~ b 의 범위가 있을 때, 새로 들어온 범위 c ~ d 가 있다고 하자.

c가 a보다 크거나 같고 d가 b보다 크다면, 범위는 a ~ d 로 갱신된다.

이런 원리고 갱신을 계속 하며 범위를 list에 담고,

list에 담긴 값들을 최종적으로 2차원 배열로 바꾸어 반환하면 해결된다. 