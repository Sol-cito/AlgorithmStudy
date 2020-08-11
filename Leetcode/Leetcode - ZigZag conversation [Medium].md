## Leetcode - ZigZag conversation [Medium]

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```

**Example 1:**

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:**

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```



Link : https://leetcode.com/problems/zigzag-conversion/



---



#### My solution (Java)

```java
class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        int numOfBlocks = s.length() / (2 * numRows - 2);
        char[][] zigzagArr = new char[(numRows - 1) * (numOfBlocks + 1)][numRows];

        int index = 0;
        for (int i = 0; i < zigzagArr.length; i++) {
            for (int j = 0; j < zigzagArr[0].length; j++) {
                if (index == s.length()) {
                    break;
                }
                if (i % (numRows - 1) == 0) {
                    zigzagArr[i][j] = s.charAt(index);
                    index++;
                } else {
                    zigzagArr[i][numRows - 1 - i % (numRows - 1)] = s.charAt(index);
                    index++;
                    break;
                }
            }
        }
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < zigzagArr[0].length; i++) {
            for (int j = 0; j < zigzagArr.length; j++) {
                if (zigzagArr[j][i] != 0) {
                    stringBuilder.append(zigzagArr[j][i]);
                }
            }
        }
        return stringBuilder.toString();
    }
}
```

---



#### My logic & Feedback

2차원 배열의 가로와 세로를 잘만 조작하면 풀 수 있는 문제.

input으로 들어오는 numRows에 따라 지그재그 모양이 결정되므로,  index를 잘 생각해서 풀면된다.

