## Leetcode - Restore IP Addresses [Medium]

Given a string `s` containing only digits, return all possible valid IP addresses that can be obtained from `s`. You can return them in **any** order.

A **valid IP address** consists of exactly four integers, each integer is between `0` and `255`, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are **valid** IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are **invalid** IP addresses. 

 

**Example 1:**

```
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
```

**Example 2:**

```
Input: s = "0000"
Output: ["0.0.0.0"]
```

**Example 3:**

```
Input: s = "1111"
Output: ["1.1.1.1"]
```

**Example 4:**

```
Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
```

**Example 5:**

```
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

 

**Constraints:**

- `0 <= s.length <= 3000`
- `s` consists of digits only.

Link : https://leetcode.com/problems/restore-ip-addresses/submissions/



---



#### My solution (Java)

```java
class Solution {
     List<String> resultList = new ArrayList<>();

    public List<String> restoreIpAddresses(String s) {
        List<String> result = new LinkedList<>();
        char[] charList = s.toCharArray();
        StringBuilder answerSB = new StringBuilder();
        recursion(charList, 0, 4, answerSB);
        return resultList;
    }

    public void recursion(char[] charList, int pointer, int remainder, StringBuilder answerSB) {
        if (remainder == 0) {
            String result = answerSB.toString();
            resultList.add(result);
            return;
        }
        int limit = charList.length;
        if (pointer + 3 <= charList.length) {
            limit = pointer + 3;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = pointer; i < limit; i++) {
            sb.append(charList[i]);
            if (charList.length - i - 1 <= 3 * (remainder - 1) && Integer.parseInt(sb.toString()) <= 255
                    && !(sb.toString().charAt(0) == '0' && sb.toString().length() > 1)) {
                int startIndex = answerSB.length();
                if (remainder == 1) {
                    answerSB.append(sb.toString());
                } else {
                    answerSB.append(sb.toString() + ".");
                }
                recursion(charList, i + 1, remainder - 1, answerSB);
                answerSB.delete(startIndex, answerSB.length());
            }
        }
    }
}
```

---



#### My logic & Feedback

기본적으로 재귀를 사용하나, 재귀를 도는 여러 조건을 추가하여 시간을 단축시키는 방법으로 풀었다.

내가 필터링한 조건은 다음과 같다 : 

1. 하나의 블럭(IP 주소는 총 4개의 블럭이 있다)의 element는 1~3개가 되어야 하므로, 다음번 재귀를 돌 때 남은 블록 * 3 (남은 element의 최대 개수) 개보다 남은 element가 많으면 재귀를 돌지 않음.
2. leading zero가 없어야 함
3. 한 블록의 숫자 크기가 255 이하여야 하며, 한 블록에는 무조건 1개 이상의 숫자가 들어가야 함.

위 조건을 if절로 하여 재귀를 선택적으로 돌게 하였고,

정답은 String으로 도출해야 하므로 시간을 단축시키기 위해 재귀 파라미터를 StringBuilder를 사용하여 시간을 단축시켰다. 

재귀를 돌 때마다 StringBuilder를 넘기는데, append  및 delete 메소드를 사용하여 참조값에서 꼬이지 않도록 구현하였다.