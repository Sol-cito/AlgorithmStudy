## Leetcode - Interleaving String [Hard]

Given `s1`, `s2`, and `s3`, find whether `s3` is formed by the interleaving of `s1` and `s2`.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg)

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
```

**Example 2:**

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
```

**Example 3:**

```
Input: s1 = "", s2 = "", s3 = ""
Output: true
```

 

**Constraints:**

- `0 <= s1.length, s2.length <= 100`
- `0 <= s3.length <= 200`
- `s1`, `s2`, and `s3` consist of lower-case English letters.

Link : https://leetcode.com/problems/interleaving-string/



---



#### My solution (Java)

```java
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s3.length() == 0) {
            return true;
        }
        return recursion(s1, 0, s2, 0, s3, 0);
    }
    public boolean recursion(String s1, int pointer1, String s2, int pointer2, String s3, int pointer3) {
        if (pointer3 == s3.length() && pointer1 == s1.length() && pointer2 == s2.length()) {
            return true;
        }
        if (pointer1 < s1.length() && pointer3 < s3.length() && s3.charAt(pointer3) == s1.charAt(pointer1)) {
            if (recursion(s1, pointer1 + 1, s2, pointer2, s3, pointer3 + 1)) {
                return true;
            }	
        }
        if (pointer2 < s2.length() && pointer3 < s3.length() && s3.charAt(pointer3) == s2.charAt(pointer2)) {
            if (recursion(s1, pointer1, s2, pointer2 + 1, s3, pointer3 + 1)) {
                return true;
            }
        }
        return false;
    }
}
```

---



#### My logic & Feedback

I solve this problem by recursive method. But I think there should be a better way such as DP (because I have peeked discussion board on the site and some people have submitted DP solutions).

Recursive formula is somewhat slow. It constantly calls the same functions and consumes large memory.

My solution is easy to come up with, but not the best solution. I must dig into DP solution for it.

