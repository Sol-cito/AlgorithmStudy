## Leetcode - Generate Parentheses [Medium]

Given *n* pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given *n* = 3, a solution set is:

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

Link : https://leetcode.com/problems/generate-parentheses/



---



#### My solution (Java)

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
 ArrayList<String> list = new ArrayList<>();

    public List<String> generateParenthesis(int n) {
        recursion(0, 0, n * 2, "");
        return list;
    }

    public void recursion(int currentNum, int openNum, int endNum, String result) {
        if (currentNum == endNum) {
            if (openNum == 0) {
                list.add(result);
            }
            return;
        }
        if (openNum > 0) {
            recursion(currentNum + 1, openNum - 1, endNum, result + ")");
            if (endNum - openNum >= openNum) {
                recursion(currentNum + 1, openNum + 1, endNum, result + "(");
            }
        } else {
            recursion(currentNum + 1, openNum + 1, endNum, result + "(");
        }
    }
}
```

---



#### My logic & Feedback

괄호 만드는 문제로, 재귀를 이용하면 간단히 풀 수 있다.

"(" 기호가 있으면 ")" 기호가 항상 뒤에 있어야 하며, "(" 기호는 n/2만큼만 만들어져야 한다.

따라서 재귀를 돌면서 "(" 기호의 개수, ")" 기호의 개수를 헤아리다가

재귀를 돈 횟수가 모든 기호의 길이 개수와 같으며 "(" 기호의 최종 개수가 0이 되는 시점에 return을 하면 된다.