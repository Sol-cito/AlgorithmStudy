## Leetcode - Surrounded Regions [Medium]

Given a 2D board containing `'X'` and `'O'` (**the letter O**), capture all regions surrounded by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

**Example:**

```
X X X X
X O O X
X X O X
X O X X
```

After running your function, the board should be:

```
X X X X
X X X X
X X X X
X O X X
```

**Explanation:**

Surrounded regions shouldn’t be on the border, which means that any `'O'` on the border of the board are not flipped to `'X'`. Any `'O'` that is not on the border and it is not connected to an `'O'` on the border will be flipped to `'X'`. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Link : https://leetcode.com/problems/surrounded-regions/

---



#### My solution (Java)

```java
class Solution {
   int flag = 1;

    public void solve(char[][] board) {
        if (board.length == 0) {
            return;
        }
        int[][] visitArr = new int[board.length][board[0].length];

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (visitArr[i][j] == 0 && board[i][j] == 'O') {
                    visitArr[i][j] = 1;
                    ArrayList<Integer> list = new ArrayList<>();
                    list.add(i);
                    list.add(j);
                    flag = 1;
                    search(board, visitArr, i, j, list);
                    if (flag == 1) {
                        flip(board, list);
                    }
                }
            }
        }
    }

    public void flip(char[][] board, ArrayList<Integer> list) {
        for (int i = 0; i < list.size(); i += 2) {
            board[list.get(i)][list.get(i + 1)] = 'X';
        }
    }

    public void search(char[][] board, int[][] visitArr, int x, int y, ArrayList<Integer> list) {
        if (x == 0 || x == board.length - 1 || y == 0 || y == board[0].length - 1) {
            flag = -1;
        }
        int[][] direction = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        for (int i = 0; i < direction.length; i++) {
            int nextX = x + direction[i][0];
            int nextY = y + direction[i][1];
            if (nextX >= 0 && nextX < board.length && nextY >= 0 && nextY < board[0].length
                    && board[nextX][nextY] == 'O' && visitArr[nextX][nextY] == 0) {
                visitArr[nextX][nextY] = 1;
                list.add(nextX);
                list.add(nextY);
                search(board, visitArr, nextX, nextY, list);
            }
        }
    }
}

```

---



#### My logic & Feedback

음...마음에 드는 풀이는 전혀 아니지만( = 성능이 별로다), 

문제를 접한 순간 바로 풀이방법이 생각나서 그냥 홀린듯이 코딩했다.

O를 만나면 search라는 메소드 재귀를 타면서 O가 있는 지역을 DFS로 탐색하며 list에 좌표를 담는다(사실 여기서 BFS로 탐색했으면 속도가 더 잘나왔겠지만, 귀찮아서...).

그러다 O가 '하나라도' border, 즉 경계선에 위치해있으면 DFS로 탐색한 좌표는 X로 바꿀 수 없으므로 나가리.

그게 아니라면 flip 메소드를 이용해 X로 바꿔주면 된다.