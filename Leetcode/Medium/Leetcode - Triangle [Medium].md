## Leetcode - Triangle [Medium]

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is `11` (i.e., **2** + **3** + **5** + **1** = 11).

**Note:**

Bonus point if you are able to do this using only *O*(*n*) extra space, where *n* is the total number of rows in the triangle.

Link : https://leetcode.com/problems/triangle/

---

#### My solution (Java)

```java
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        List<List<Integer>> cloneList = new ArrayList<>();
        for (int i = 0; i < triangle.size(); i++) {
            cloneList.add(new ArrayList<>());
        }
        cloneList.get(0).add(triangle.get(0).get(0));
        for (int i = 1; i < triangle.size(); i++) {
            for (int j = 0; j < triangle.get(i).size(); j++) {
                if (j == 0) {
                    cloneList.get(i).add(triangle.get(i).get(j) + cloneList.get(i - 1).get(j));
                } else if (j > 0 && j < triangle.get(i).size() - 1) {
                    if (cloneList.get(i - 1).get(j - 1) >= cloneList.get(i - 1).get(j)) {
                        cloneList.get(i).add(triangle.get(i).get(j) + cloneList.get(i - 1).get(j));
                    } else {
                        cloneList.get(i).add(triangle.get(i).get(j) + cloneList.get(i - 1).get(j - 1));
                    }
                } else {
                    cloneList.get(i).add(triangle.get(i).get(j) + cloneList.get(i - 1).get(j - 1));
                }
            }
        }
        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < cloneList.get(cloneList.size() - 1).size(); i++) {
            answer = Math.min(answer, cloneList.get(cloneList.size() - 1).get(i));
        }
        return answer;
    }
}
```

---

#### My logic & Feedback

나는 위에서부터 푸는 방법을 택했으나, 대다수의 유저들이 bottom up 방식으로 푼 것 같다.

다른 사람들의 코드를 읽고 이해해보니, Bottom up 방식이 훨씬 편하고, 코드량도 줄고, memory를 더욱 줄일 수 있다.

가장 아래 row에서 위로 올라갈 때, 자신과 동일한 index, index + 1 의 두 element를 비교해서 최소값이 되는 element를 선택하면 된다.

이 문제는 프로그래머스에도 비슷한 문제가 있었던 것 같은데..그때는 내가 Bottom up 으로 접근했던 것 같다(아닌가..?).





