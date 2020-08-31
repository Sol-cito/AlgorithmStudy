## Leetcode - Valid Sudoku [Medium]

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the 9 `3x3` sub-boxes of the grid must contain the digits `1-9` without repetition.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)
A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character `'.'`.

**Example 1:**

```
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
```

**Example 2:**

```
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

**Note:**

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
- The given board contain only digits `1-9` and the character `'.'`.
- The given board size is always `9x9`.

Link : https://leetcode.com/problems/valid-sudoku/



---



#### My solution (Java)

```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        if (validateHorizontalAndVertical(board.length, board.length, board)
                && validateBlocks(board.length, board.length, board)) {
            return true;
        }
        return false;
    }

    public boolean validateBlocks(int x, int y, char[][] board) {
        int point_horizontal = 0;
        int point_vertical = 0;
        for (int m = 0; m < 3; m++) {
            point_horizontal = 0;
            for (int k = 0; k < 3; k++) {
                HashSet<Character> set = new HashSet<>();
                for (int i = point_horizontal; i < point_horizontal + 3; i++) {
                    for (int j = point_vertical; j < point_vertical + 3; j++) {
                        if (board[i][j] != '.') {
                            if (!set.contains(board[i][j])) {
                                set.add(board[i][j]);
                            } else {
                                return false;
                            }
                        }
                    }
                }
                point_horizontal += 3;
            }
            point_vertical += 3;
        }
        return true;
    }

    public boolean validateHorizontalAndVertical(int x, int y, char[][] board) {
        for (int i = 0; i < board.length; i++) {
            HashSet<Character> set1 = new HashSet<>();
            HashSet<Character> set2 = new HashSet<>();
            for (int j = 0; j < board.length; j++) {
                if (board[i][j] != '.') {
                    if (!set1.contains(board[i][j])) {
                        set1.add(board[i][j]);
                    } else {
                        return false;
                    }
                }
                if (board[j][i] != '.') {
                    if (!set2.contains(board[j][i])) {
                        set2.add(board[j][i]);
                    } else {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
```

---



#### My logic & Feedback

For문으로 범위 설정을 하는 구현력을 보는 문제.

딱히 어려운 점은 없고, set을 이용해 중복검사만 잘 해주면 된다.

for문을 많이 쓰다보니 코드가 좀 더러운데, 조금 더 깔끔하게 표현할 수 있는 방법이 없을까?