## Leetcode - Word Ladder [Medium]

Given two words (*beginWord* and *endWord*), and a dictionary's word list, find the length of shortest transformation sequence from *beginWord* to *endWord*, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list.

**Note:**

- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume *beginWord* and *endWord* are non-empty and are not the same.

**Example 1:**

```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
```

**Example 2:**

```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```



Link : https://leetcode.com/problems/word-ladder/

---



#### My solution (Java)

```java
class Solution {
 public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Queue<String> que = new LinkedList<>();
        que.add(beginWord);
        HashMap<String, Integer> depthMap = new HashMap<>();
        HashMap<String, Boolean> checkMap = new HashMap<>();
        depthMap.put(beginWord, 1);
        checkMap.put(beginWord, true);

        while (!que.isEmpty()) {
            String polled = que.poll();
            if (polled.equals(endWord)) {
                return depthMap.get(polled);
            }
            for (int i = 0; i < wordList.size(); i++) {
                if (checkMap.get(wordList.get(i)) == null && compare(polled, wordList.get(i))) {
                    depthMap.put(wordList.get(i), depthMap.get(polled) + 1);
                    que.add(wordList.get(i));
                    checkMap.put(wordList.get(i), true);
                }
            }
        }
        return 0;
    }

    public boolean compare(String a, String b) {
        int count = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                count++;
            }
            if (count > 1) {
                return false;
            }
        }
        return true;
    }
}

```

---



#### My logic & Feedback

전형적인 BFS...인데 HashMap을 2개나 사용했더니 메모리 및 속도 낭비가 심하다.

BFS를 오랜만에 풀어서 처음에 약간 헤멨다. Depth를 어떻게 넣을지를 잘 구상해야 하는 문제다.