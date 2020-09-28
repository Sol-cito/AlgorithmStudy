## Leetcode - Shortest Palindrome [Hard]

Given a string ***s***, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

**Example 1:**

```
Input: "aacecaaa"
Output: "aaacecaaa"
```

**Example 2:**

```
Input: "abcd"
Output: "dcbabcd"
```



Link : https://leetcode.com/problems/shortest-palindrome/



---

#### My solution (Java)

```java
class Solution {
     public String shortestPalindrome(String s) {
        int lastIndex = s.length();
        int diffCnt = -1;
        while (diffCnt != 0) {
            diffCnt = 0;
            for (int i = 0, j = lastIndex - 1; i < j; i++, j--) {
                if (s.charAt(i) != s.charAt(j)) {
                    diffCnt++;
                    break;
                }
            }
            lastIndex--;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = s.length() - 1; i > lastIndex; i--) {
            sb.append(s.charAt(i));
        }
        return sb.append(s).toString();
    }
}
```

---

#### My logic & Feedback

This solution is not so fast, but consumes less memory and very easy to understand.

Firstly set up two points, i and j in the for loop. The pointer i starts from index 0 and j from the last index.

Since the condition of the problem is 'adding characters in front of it', if it turns not to be palindrome, j gets pulled back by one index (lastIndex--).

It keeps doing it until it finds the moment some range of the word can be palindrome, and that's where the new word is born by StringBuilder.

The time complexity is O(N^2). Is there any other faster solution?



