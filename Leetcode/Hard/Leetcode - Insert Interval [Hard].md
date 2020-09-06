## Leetcode - Insert Interval [Hard]

Given a set of *non-overlapping* intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

**Example 1:**

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2:**

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.출처 

Link: https://leetcode.com/problems/insert-interval/



---



#### My solution (Java)

```java
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int[][] answer = null;

        if (newInterval.length == 0) {
            return intervals;
        }
        if (intervals.length == 0 || intervals[0].length == 0) {
            answer = new int[1][2];
            answer[0] = newInterval;
            return answer;
        }
        for (int i = 0; i < intervals.length; i++) {
            if (intervals[i][0] <= newInterval[0] && intervals[i][1] >= newInterval[0]) {
                newInterval[0] = intervals[i][0];
            }
            if (intervals[i][0] <= newInterval[1] && intervals[i][1] >= newInterval[1]) {
                newInterval[1] = intervals[i][1];
            }
        }
        ArrayList<Integer> list = new ArrayList<>();
        list.add(newInterval[0]);
        list.add(newInterval[1]);
        for (int i = 0; i < intervals.length; i++) {
            if (intervals[i][0] > newInterval[1] || intervals[i][1] < newInterval[0]) {
                list.add(intervals[i][0]);
                list.add(intervals[i][1]);
            }
        }
        Collections.sort(list);

        answer = new int[list.size() / 2][2];
        for (int i = 0; i < list.size(); i++) {
            answer[i / 2][i % 2] = list.get(i);
        }
        return answer;
    }
}

```

---



#### My logic & Feedback

I was trying to solve it with hash map, storing all the **opening and closing indexes** (in a given interval array [0,3] for instance, 0 is opening and 3 is closing one from my logic) counting when facing each index and finally figuring out **on which index the count number turns into 0 or 1**.

But facing many counterexamples, I pivoted to simpler approach..

Main idea is, updating newInterval values by looping all given intervals so that I figure out what new range will be set up at the end.

Afterwards, do the same loop once again and store indexes, which are not absorbed by the new range, into a list.

Sort the list, copying the values into a new array, and return it.

