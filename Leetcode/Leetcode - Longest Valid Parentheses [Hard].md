## Leetcode - Longest Valid Parentheses [Hard]

Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.

**Example 1:**

```
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
```

**Example 2:**

```
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
```

Link : https://leetcode.com/problems/longest-valid-parentheses/



---



#### My solution (Java)

```java
class Solution {
        public int longestValidParentheses(String s) {
        int answer = 0;
        int[] checkArr = new int[s.length()];
        Stack<Character> parenthesesStack = new Stack<>();
        Stack<Integer> indexStack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                parenthesesStack.add(s.charAt(i));
                indexStack.add(i);
            } else {
                if (!parenthesesStack.isEmpty() && parenthesesStack.peek() == '(') {
                    parenthesesStack.pop();
                    checkArr[indexStack.pop()] = 1;
                    checkArr[i] = 1;
                }
            }
        }
        int cnt = 0;
        for (int i = 0; i < checkArr.length; i++) {
            if (checkArr[i] == 1) {
                cnt++;
            } else {
                answer = Math.max(answer, cnt);
                cnt = 0;
            }
        }
        answer = Math.max(answer, cnt);
        return answer;
    }
}

```

---



#### My logic & Feedback

The point is to use two stack, one of which is to store each parentheses' index and the other for the character itself.

Using stack, we can figure out when valid parentheses are created.

But we also have to save the length between them to lay out answer.

That's why I put an integer array and another stack to figure out which index parentheses point out and to mark their index.

After looping entire input string, all we have to do is just to count the longest length by looking into the array with the value of one.