## Leetcode -Palindrome Partitioning [Medium]

Given a string *s*, partition *s* such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of *s*.

**Example:**

```
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
```

Link : https://leetcode.com/problems/palindrome-partitioning/



---



#### My solution (Java)

```java
class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> answer = new LinkedList<>();
        recursion(s, new LinkedList<>(), answer);
        return answer;
    }

    public void recursion(String s, LinkedList<String> list, List<List<String>> answer) {
        if (s.length() == 0) {
            answer.add(list);
            return;
        }
        for (int i = s.length(); i >= 1; i--) {
            String sub = s.substring(0, i);
            if (isPalindrome(sub)) {
                list.add(sub);
                recursion(s.substring(i), new LinkedList<>(list), answer);
                list.removeLast();
            }
        }
    }

    public boolean isPalindrome(String s) {
        for (int i = 0, j = s.length() - 1; i <= j; i++, j--) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
        }
        return true;
    }
}

```

---



#### My logic & Feedback

쉬운 문제...substring으로 단어를 계속 자르면서 substring 된 단어가 palindrome 인지 검사하면 된다.

palindrome이면 잘라내고 남은 부분을 다시 재귀로 돌면 쉽게 끝난다.

substring을 썼으니 사실 효율적인 문제풀이는 아니다. substring자체가 느리니...

substring보다는 StringBuilder를 통해 char를 하나씩 붙여서 재귀를 돌면 되지만, 

풀이 로직 자체는 본질적으로 같기 때문에 그냥 이렇게 마무리하였다. 