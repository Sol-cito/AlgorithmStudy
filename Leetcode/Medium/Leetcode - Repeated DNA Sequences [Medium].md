## Leetcode - Repeated DNA Sequences [Medium]

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

**Example:**

```
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
```

Link : https://leetcode.com/problems/repeated-dna-sequences/submissions/

---



#### My solution (Java)

```java
class Solution {
   public List<String> findRepeatedDnaSequences(String s) {
        ArrayList<String> list = new ArrayList<>();
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < s.length() - 9; i++) {
            String target = s.substring(i, i + 10);
            if (set.contains(target) && !list.contains(target)) {
                list.add(target);
            } else {
                set.add(target);
            }
        }
        return list;
    }
}
```

---



#### My logic & Feedback

list와 set을 이용하면 너무나 쉽게 풀수 있는 문제...이건 난이도 Easy 아닌가? 

왜 Medium에 있는지 모르겠다.