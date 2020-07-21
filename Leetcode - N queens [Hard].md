## Leetcode - N queens [Hard]

The *n*-queens puzzle is the problem of placing *n* queens on an *n*×*n* chessboard such that no two queens attack each other.

![img](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)

Given an integer *n*, return all distinct solutions to the *n*-queens puzzle.

Each solution contains a distinct board configuration of the *n*-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space respectively.

**Example:**

```
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
```

출처 : https://leetcode.com/problems/n-queens/



---



#### My solution (Java)

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    ArrayList<ArrayList<Integer>> result = new ArrayList<>();

    public List<List<String>> solveNQueens(int n) {
        int[][] chessBoard = new int[n][n];
        ArrayList<Integer> list = new ArrayList<>();
        putChess(n, 0, chessBoard, list);
        List<List<String>> answer = new ArrayList<>();

        for (ArrayList<Integer> eachList : result) {
            ArrayList<String> result = new ArrayList<>();
            for (int i = 0; i < eachList.size(); i++) {
                int num = eachList.get(i);
                String addTarget = "";
                for (int j = 0; j < n; j++) {
                    if (j == num) {
                        addTarget += "Q";
                    } else {
                        addTarget += ".";
                    }
                }
                result.add(addTarget);
            }
            answer.add(result);
        }
        return answer;
    }

    public void putChess(int n, int lineNum, int[][] chessBoard, ArrayList<Integer> list) {
        if (lineNum == n) { // return when all the required queens has been located
            result.add(list);
            return;
        }
        int[][] copied = new int[n][n];
        for (int i = 0; i < n; i++) { // put a queen on [lineNum][i]
            if (chessBoard[lineNum][i] == 0) { // if the location is 0
                for (int j = 0; j < chessBoard.length; j++) { // copy board arr
                    for (int k = 0; k < chessBoard.length; k++) {
                        copied[j][k] = chessBoard[j][k];
                    }
                }
                // check all spots on the horizontal and vertical line from the queen
                for (int j = 0; j < n; j++) {
                    copied[lineNum][j] = 1; // vertical
                    copied[j][i] = 1; // horizontal
                }
                int[][] directions = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
                for (int j = 0; j < directions.length; j++) {
                    int multiply = 0;
                    int x = lineNum;
                    int y = i;
                    // check all spots on the diagnal line from the queen
                    while (x >= 0 && x < n && y >= 0 && y < n) {
                        copied[x][y] = 1;
                        x = lineNum + multiply * directions[j][0];
                        y = i + multiply * directions[j][1];
                        multiply++;
                    }
                }
                // insert queen in a new ArrayList and do recursion
                ArrayList<Integer> newList = new ArrayList<>();
                for (int each : list) {
                    newList.add(each);
                }
                newList.add(i);
                putChess(n, lineNum + 1, copied, newList);
            }
        }
    }
}
```

---



#### My logic & Feedback

TCT 4번 에 위 문제와 비슷하나 응용된 문제가 나왔고, 결국 풀지못한 나머지 분해서 풀어본 문제...

구글에 검색해보니 '**백트래킹'**이라는 용어가 나와서 순간 내가 모르는 알고리즘 풀이법인가? 생각했는데,

그냥 이전에 탐색했던 것을 다음 번 탐색 때 반영하는 개념이었다...괜히 영어로 말을 어렵게 해서 헷갈리는듯.

아무튼, n개의 퀸은 상하좌우로 움직이기 때문에 한 줄에 하나밖에 놓지 못한다.

또한, 대각선에 있는 모든 점 위에는 다른 퀸을 놓지 못하기 때문에 퀸을 한 줄에 하나 놓을 때 마다 

전체 board 배열의 해당 대각선을 1로 처리해주면 된다.

재귀를 돌면서 체스판에 n개의 퀸을 다 넣었을 때 return하면 답이다. 

재귀 탐색의 전형적인 문제라 그렇게 어렵지는 않았는데...

TCT를 풀 때에는 바보같이 퀸 하나를 놓았을 때 나머지 경우의 수를 재귀로 다 구하는 바람에 시간초과가 났다.

퀸 하나를 놓고 다음 퀸을 놓을 때 이전 퀸으로 인해 놓지 못하는 경우를 고려를 하지 않아 엄청나게 많은 경우의 수가 발생해버린 것...

