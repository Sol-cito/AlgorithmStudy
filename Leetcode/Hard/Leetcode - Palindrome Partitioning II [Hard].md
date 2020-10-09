## Leetcode - Palindrome Partitioning II [Hard]

Given a string `s`, partition `s` such that every substring of the partition is a palindrome.

Return *the minimum cuts needed* for a palindrome partitioning of `s`.

 

**Example 1:**

```
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
```

**Example 2:**

```
Input: s = "a"
Output: 0
```

**Example 3:**

```
Input: s = "ab"
Output: 1
```

 

**Constraints:**

- `1 <= s.length <= 2000`
- `s` consists of lower-case English letters only.

 

Link: https://leetcode.com/problems/palindrome-partitioning-ii/



---

#### My solution (Java) - BFS

```java
class Solution {
	 public int minCut(String s) {
        Queue<String> que = new LinkedList<>();
        Set<String> set = new HashSet<>();
        LinkedList<Integer> linkedList = new LinkedList<>();
        que.add(s);
        linkedList.add(0);
        while (!que.isEmpty()) {
            String polled = que.poll();
            if (isPalindrome(polled)) {
                return linkedList.getFirst();
            }
            splitAndPut(polled, que, linkedList, linkedList.getFirst() + 1, set);
            linkedList.removeFirst();
        }
        return 0;
    }

    public void splitAndPut(String target, Queue<String> que, LinkedList<Integer> LinkedList, int newDepth, Set<String> set) {
        for (int i = target.length() - 1; i >= 1; i--) {
            String sub = target.substring(i);
            if (isPalindrome(target.substring(0, i)) && !set.contains(sub)) {
                que.add(target.substring(i));
                LinkedList.add(newDepth);
                set.add(target.substring(i));
            }
        }
    }

    public boolean isPalindrome(String target) {
        for (int i = 0, j = target.length() - 1; i < j; i++, j--) {
            if (target.charAt(i) != target.charAt(j)) {
                return false;
            }
        }
        return true;
    }
}
```

---

#### My logic & Feedback

This problem can be solved by BFS approach.

Input String can be split into various substrings which can possibly be a palindrome. 

Every substring of which palindromic part has been cut away is inserted into Queue over and over, and their depth is stored in LinkedList at the same time.

Continuously pulling out an element from Queue, when the entire String is palindromic, return its depth (the number of cuts)

It's easy approach. 

But I saw DP solution in the discussion of Leetcode website, which is neater than my approach.

The link is https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42213/Easiest-Java-DP-Solution-(97.36)

The main idea of this DP solution is, **to refer to previous cut and to keep returning the minimum cut by comparing**.

```
String pal = "ab/cbabc/e";
int[] cuts = new int[pal.length];
```

For example, given a string above, we can see there one palindrome whose length > 1.

When it's found, compare **how many cuts need to split each character** and **cut[current char index - 1] + 1** to find out the minimum number of cut on that spot.

In short, **store the minimum number of cuts and refer to it every time**.

Truly amazing, so I have to bear it in mind for the future.

 



