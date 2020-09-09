## Leetcode - Reverse Words in a String [Medium]

Given an input string, reverse the string word by word.

 

**Example 1:**

```
Input: "the sky is blue"
Output: "blue is sky the"
```

**Example 2:**

```
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

**Example 3:**

```
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

 

**Note:**

- A word is defined as a sequence of non-space characters.
- Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
- You need to reduce multiple spaces between two words to a single space in the reversed string.

Link : https://leetcode.com/problems/validate-binary-search-tree/

---



#### My solution (Java)

```java
class Solution {
    public String reverseWords(String s) {
        LinkedList<String> linkedList = new LinkedList<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                linkedList.addFirst(sb.toString().trim());
                sb = new StringBuilder();
            } else {
                sb.append(s.charAt(i));
            }
        }
        linkedList.addFirst(sb.toString());
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < linkedList.size(); i++) {
            if (linkedList.get(i).length() > 0) {
                answer.append(linkedList.get(i) + " ");
            }
        }
        return answer.toString().trim();
    }
}
```

---



#### My logic & Feedback

StringBuilder와 Trim, LinkedList를 이용하면 적당히 잘 풀 수 있는 문제다.

순서를 뒤집어야 하니 LinkedList의 addFirst 기능을 이용하였고, 공백제거를 위해 trim 및 적절한 포인터를 사용하였다.

쉬운문제인데 왜 좋아요보다 싫어요가 더 많지?