## Leetcode - Decode ways [Medium]

A message containing letters from `A-Z` is being encoded to numbers using the following mapping:

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

Given a **non-empty** string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a **32-bit** integer.

 

**Example 1:**

```
Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
```

**Example 2:**

```
Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

**Example 3:**

```
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.
```

**Example 4:**

```
Input: s = "1"
Output: 1
```

 

**Constraints:**

- `1 <= s.length <= 100`
- `s` contains only digits and may contain leading zero(s).

Link : https://leetcode.com/problems/decode-ways/

---



#### My solution (Java)

```java
class Solution {
   public int numDecodings(String s) {
        if (s.length() < 2 || s.charAt(0) == '0') {
            return s.charAt(0) == '0' ? 0 : 1;
        }
        int f1 = s.charAt(0) != '0' ? 1 : 0;
        int f2 = getNumTwo(s.substring(0, 2));
        int f3 = f2;
        for (int i = 2; i < s.length(); i++) {
            f1 = s.charAt(i - 1) != '0' && Integer.parseInt(s.substring(i - 1, i + 1)) <= 26 ? f1 : 0;
            f2 = s.charAt(i) != '0' ? f2 : 0;
            f3 = f1 + f2;
            f1 = f2;
            f2 = f3;
        }
        return f3;
    }

    public int getNumTwo(String num) {
        if (num.charAt(0) == '0') {
            return 0;
        } else if (num.charAt(1) == '0') {
            if (num.charAt(0) == '1' || num.charAt(0) == '2') {
                return 1;
            } else {
                return 0;
            }
        } else if (Integer.parseInt(num) > 26) {
            return 1;
        }
        return 2;
    }
}
```

---



#### My logic & Feedback

아..이 악마의 문제...

12번의 제출 전부 실패(시간초과 3번), 결국 Accepted 되었다.

처음에 재귀 완전탐색으로 접근했다가 시간초과가 나서....

곰곰히 풀이방법을 생각하다가 DP Solution 을 생각해냈다.

예를 들어 "12654"라는 길이 주어졌다고 하자.

맨 처음 '1'을 갈 수 있는 방법은 1개다. -> f1

그 다음 '12'을 갈 수 있는 방법은 2개다 (17과 1/7) -> f2

그리고, '126'를 갈 수 있는 방법은 **'26'이 들어온다고 생각했을 때, 1까지 갈 수 있는 방법의 개수' + '12까지 갈 수 있는 방법의 개수' **로 나타낼 수 있다.

즉 F3 = F2 + F1 인, 전형적인 DP다.

여기서 문제는 다음 수가 '26'이 아니거나 '0'인 경우인데, 이 두 가지 조건떄문에 수 많은 테스트케이스에서 실패를 맛봤다.

어찌어찌 통과하긴 했지만, 그래도 뭔가 코드가 깔끔하지는 않다.

**그러나 속도가 97%가 나왔다는 것!!**

이 문제를 푸는데 거의 4시간이 걸렸는데, 

이 문제를 풀면서 3항 연산자 및 DP 사고방식을 4시간동안 공부했다고 생각하자..