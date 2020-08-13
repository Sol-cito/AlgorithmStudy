## Leetcode - Integer to Roman [Medium]

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

**Example 1:**

```
Input: "()"
Output: true
```

**Example 2:**

```
Input: "()[]{}"
Output: true
```

**Example 3:**

```
Input: "(]"
Output: false
```

**Example 4:**

```
Input: "([)]"
Output: false
```

**Example 5:**

```
Input: "{[]}"
Output: true
```

Link : https://leetcode.com/problems/valid-parentheses/



---



#### My solution (Java)

```java
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (stack.isEmpty()) {
                stack.add(s.charAt(i));
            } else {
                char peeked = stack.peek();
                if (s.charAt(i) != peeked && Math.abs(s.charAt(i) - peeked) < 3) {
                    stack.pop();
                } else {
                    stack.add(s.charAt(i));
                }
            }
        }
        if (stack.isEmpty()) {
            return true;
        }
        return false;
    }
}
```

---



#### My logic & Feedback

In my point of view, the question is to test if the participant has a knowledge of stack.

All you have to do is, to point each character of string s, see if they have to be put in the stack or match with the one on the top of the stack.

Return value depends on if the stack is empty (if the parentheses has been properly closed).

