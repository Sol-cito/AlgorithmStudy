## Leetcode - Word Break [Medium]

Given a **non-empty** string *s* and a dictionary *wordDict* containing a list of **non-empty** words, determine if *s* can be segmented into a space-separated sequence of one or more dictionary words.

**Note:**

- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

**Example 1:**

```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2:**

```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```

**Example 3:**

```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

- Link : https://leetcode.com/problems/word-break/

---



#### My solution (Java)

```java
class Solution {   
	public boolean wordBreak(String s, List<String> wordDict) {
        return recursion(s, wordDict, new HashSet<>());
    }

    public boolean recursion(String s, List<String> wordDict, Set<String> set) {
        if (s.length() == 0) return true;
        for (String word : wordDict) {
            if (s.startsWith(word) && !set.contains(s.substring(word.length()))) {
                set.add(s.substring(word.length()));
                if (recursion(s.substring(word.length()), wordDict, set)) return true;
            }
        }
        return false;
    }
}
```

---



#### My logic & Feedback

처음에 풀이방법이 생각나지 않아 조금 헤멨다.

분명히 재귀를 통한 완전탐색인거 같은데...구현을 해도 Time Limit Exceeds가 나왔다. 

고민하던 중, Time Limit Exceeds가 나온 테스트 케이스를 보니

완전탐색의 경우 중복되는 탐색값이 많아 시간초과가 날 수 밖에 없었다.

예를 들어 

```
String s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab";
List<String> wordDict = {"a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa"}
```

의 경우, "a"로 최초 재귀를 타서 쭈욱 가다가 맨 마지막에 b때문에 막히게 된다.

그 후 "aa"로 다시 재귀를 타기 시작하는데, 

사실 "aa"가 탐색하는 s의 부분은 이미 "a"가 탐색을 하였으며, '안된다'고 결론이 난 부분이다(다른 element도 마찬가지).

따라서 Set 을 이용하여, 기존에 유효하다고 판정이 난 부분은 set에 담고, 

다음 element가 재귀를 타기 시작할 때는 set에 담긴 부분을 제외하고 재귀를 돌리는 것이 반복 횟수를 줄이는 방법이다.

따라서 이 풀이방법은 Backtracking(퇴각검색)이 될 것 같다. 