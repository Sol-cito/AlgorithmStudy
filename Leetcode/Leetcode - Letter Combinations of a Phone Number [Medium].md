## Leetcode - Integer to Roman [Medium]

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

**Example:**

```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

**Note:**

Although the above answer is in lexicographical order, your answer could be in any order you want.

Link : https://leetcode.com/problems/letter-combinations-of-a-phone-number/



---



#### My solution (Java)

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Solution {
    List<String> resultList = new ArrayList<>();

    public List<String> letterCombinations(String digits) {
        HashMap<Integer, List<Character>> map = new HashMap();
        String alpha = "abcdefghijklmnopqrstuvwxyz";
        int indexPoint = 0;
        for (int i = 2; i <= 9; i++) {
            int numOfInput = 0;
            if (i == 7 || i == 9) {
                numOfInput = 4;
            } else {
                numOfInput = 3;
            }
            List<Character> list = new ArrayList<>();
            for (int j = 0; j < numOfInput; j++) {
                list.add(alpha.charAt(indexPoint));
                indexPoint++;
            }
            map.put(i, list);
        }
        if (digits.length() > 1) {
            recursion(digits, 0, map, "");
        }
        return resultList;
    }

    public void recursion(String digits, int index, HashMap<Integer, List<Character>> map, String result) {
        if (index == digits.length()) {
            resultList.add(result);
            return;
        }
        int mapKey = Integer.parseInt("" + digits.charAt(index));
        for (int i = 0; i < map.get(mapKey).size(); i++) {
            recursion(digits, index + 1, map, result + map.get(mapKey).get(i));
        }
    }
}

```

---



#### My logic & Feedback

문제를 보자마자 풀이방법이 생각날 정도로 쉬운 문제.

나는 Map과 재귀의 조합으로 풀었다.



