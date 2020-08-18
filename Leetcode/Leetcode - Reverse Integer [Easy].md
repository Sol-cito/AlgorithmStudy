## Leetcode - Reverse Integer [Easy]

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**

```
Input: 123
Output: 321
```

**Example 2:**

```
Input: -123
Output: -321
```

**Example 3:**

```
Input: 120
Output: 21
```

**Note:**
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Link : https://leetcode.com/problems/reverse-integer/



---



#### My solution (Java)

```java
class Solution {
   public int reverse(int x) {
        String target = "" + x;
        StringBuilder sb = new StringBuilder();
        int endPoint = 0;
        if (target.charAt(0) == '-') {
            sb.append('-');
            endPoint++;
        }
        for (int i = target.length() - 1; i >= endPoint; i--) {
            sb.append(target.charAt(i));
        }
        try {
            return Integer.parseInt(sb.toString());
        } catch (Exception e) {
            return 0;
        }
    }
}
```

---



#### My logic & Feedback

풀이 방법이 여러가지 있겠지만,

주어진 x를 String으로 바꾸고 charAt으로 한글자 한글자씩 보면서 StringBuilder에 거꾸로 넣어준 후,

Integer.parseInt로 형변환해주면 끝이다.

물론 overflow를 대비하여 try~catch로 감싸주어야 함.