## Leetcode - Integer to Roman [Medium]

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, two is written as `II` in Roman numeral, just two one's added together. Twelve is written as, `XII`, which is simply `X` + `II`. The number twenty seven is written as `XXVII`, which is `XX` + `V` + `II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

**Example 1:**

```
Input: 3
Output: "III"
```

**Example 2:**

```
Input: 4
Output: "IV"
```

**Example 3:**

```
Input: 9
Output: "IX"
```

**Example 4:**

```
Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
```

**Example 5:**

```
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

Link : https://leetcode.com/problems/integer-to-roman/



---



#### My solution (Java)

```java
class Solution {
   public String intToRoman(int num) {
            StringBuilder sb = new StringBuilder();
            int[] arr = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000, 4000};
            String[] strArr = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
            while (num > 0) {
                for (int i = 0; i < arr.length; i++) {
                    if (num < arr[i]) {
                        int quotient = num / arr[i - 1];
                        for (int j = 0; j < quotient; j++) {
                            sb.append(strArr[i - 1]);
                        }
                        num = num % arr[i - 1];
                        break;
                    }
                }
            }
            return sb.toString();
        }
}
```

---



#### My logic & Feedback

얼핏 보면 어려워보이나, 몫과 나머지를 이용하면 쉽게 풀리는 문제.

최대값이 3999로 고정되어있고 쓸 수 있는 숫자가 한정되어 있기 때문에,

몫대로 strArr에 있는 수를 index를 통해 넣고,  나머지는 또 다시 반복하여 풀면 된다.



