## Leetcode - Word Search [Medium]

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example:**

```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
```

 

**Constraints:**

- `board` and `word` consists only of lowercase and uppercase English letters.
- `1 <= board.length <= 200`
- `1 <= board[i].length <= 200`
- `1 <= word.length <= 10^3`

Link : https://leetcode.com/problems/word-search/



---



#### My solution (Java)

```java
class Solution {
   public boolean exist(char[][] board, String word) {
        char firstChar = word.charAt(0);
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == firstChar) {
                    int[][] visitCheck = new int[board.length][board[0].length];
                    visitCheck[i][j] = 1;
                    if (recursion(board, word, 1, i, j, visitCheck)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public boolean recursion(char[][] board, String word, int wordIndex, int x, int y, int[][] visitCheck) {
        if (wordIndex == word.length()) {
            return true;
        }
        int[][] direction = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        for (int i = 0; i < direction.length; i++) {
            int nextX = x + direction[i][0];
            int nextY = y + direction[i][1];
            if (nextX >= 0 && nextX < board.length && nextY >= 0 && nextY < board[0].length
                    && visitCheck[nextX][nextY] == 0 && board[nextX][nextY] == word.charAt(wordIndex)) {
                visitCheck[nextX][nextY] = 1;
                if (recursion(board, word, wordIndex + 1, nextX, nextY, visitCheck)) {
                    return true;
                }
                visitCheck[nextX][nextY] = 0;
            }
        }
        return false;
    }
}

```

---



#### My logic & Feedback

DFS 문제이며, 재귀로 접근했다.

이 문제를 풀면서 2가지를 배웠다.

1. 재귀문제를 풀면 항상 Array를 복사하곤 했는데, 그럴필요가 없다는 사실을 다른 사람의 코드를 보고 깨달았다. 재귀가 분기할 때 visitCheck 배열의 타겟을 1로 만들면 그 아래 분기들은 전부 그 주소값을 참조하므로 반영이 되지만, 재귀를 돌고난 후 다시 visitCheck 타겟을 0으로 바꿔버리면 다음 분기에는 영향을 미치지 않는다. 따라서 앞으로는 array를 복사하는 뻘짓과 시간낭비를 하지 않아도 된다.

2. 재귀를 탈출할 때, 

   ```
   if (recursion(board, word, wordIndex + 1, nextX, nextY, visitCheck)) {
       return true;
   }
   ```

   위와 같은 코드를 쓰면 메소드의 마지막 return false의 영향을 받지 않고 메소드가 종료된다.

   따라서 코드가 훨씬 직관적이고 깔끔하게 표현된다.

   앞으로 재귀를 쓸 때 탈출조건으로 반드시 저런식으로 작성하도록 하자.

