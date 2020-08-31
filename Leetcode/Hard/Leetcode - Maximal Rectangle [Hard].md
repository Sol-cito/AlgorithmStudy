## Leetcode - Maximal Rectangle [Hard]

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

**Example:**

```
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
```

Link : https://leetcode.com/problems/maximal-rectangle/



---



#### My solution (Java)

```java
class Solution {
   public int maximalRectangle(char[][] matrix) {
        int answer = 0;
        if (matrix.length == 0 || matrix[0].length == 0) {
            return answer;
        }
        for (int i = matrix[0].length; i > 0; i--) {
            for (int j = 0; j < matrix.length; j++) {
                for (int k = 0; k <= matrix[0].length - i; k++) {
                    if (checkIfAllOne(matrix, j, k, k + i - 1)) {
                        answer = Math.max(answer, measureSizeOfRectangle(matrix, j, k, k + i - 1));
                    }
                }
            }
        }
        return answer;
    }

    public int measureSizeOfRectangle(char[][] matrix, int lineNum, int startPoint, int endPoint) {
        int initialValue = endPoint - startPoint + 1;
        int size = initialValue;
        for (int i = lineNum + 1; i < matrix.length; i++) {
            if (checkIfAllOne(matrix, i, startPoint, endPoint)) {
                size += initialValue;
            } else {
                return size;
            }
        }
        return size;
    }

    public boolean checkIfAllOne(char[][] matrix, int lineNum, int startPoint, int endPoint) {
        for (int i = startPoint; i <= endPoint; i++) {
            if (matrix[lineNum][i] == '0') {
                return false;
            }
        }
        return true;
    }
}
```

---



#### My logic & Feedback

My approach is brute force, even though I was feeling that there should be a way to solve this by dynamic programming or greedy.

As it turned out, this approach is not that fast as I expected, so I must look for other solutions on website later on.

Anyhow, the idea is to search valid rectangle by searching all line length from the top (from the maximum valid length to the minimum by using for loop) and verifying the same length could be found below.

Once a valid (only containing '1') line is found, the algorithm starts to look at the lines below in order to measure the entire size of rectangle. 

For example, if the algorithm finds a line whose length is three ('0', '1', '1', '1', '0'), it will see the next lines from the same start index to the end index to verify it also has the same number of '1', and it will keep doing it for the next line until it reaches out the very last line.

If one of the lines has '0' on the range, the searching operation stops and returns the value of the size which had been calculated until it stops.

The values are to be compared by Math. function to only pick up the largest number.