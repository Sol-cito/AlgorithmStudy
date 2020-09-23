## Leetcode - Word Search II [Hard]

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

**Example:**

```
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
```



Link : https://leetcode.com/problems/word-search-ii/

---



#### My solution (Java)

```java
class Solution {
  List<String> answer = new ArrayList<>();

    public List<String> findWords(char[][] board, String[] words) {
        for (String eachWord : words) {
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[0].length; j++) {
                    if (board[i][j] == eachWord.charAt(0)) {
                        int[][] visitCheck = new int[board.length][board[0].length];
                        visitCheck[i][j] = 1;
                        checkIfMatches(board, eachWord, 1, i, j, visitCheck);
                    }
                }
            }
        }
        return answer;
    }

    public void checkIfMatches(char[][] board, String word, int charPointer, int x, int y, int[][] visitCheck) {
        if (charPointer >= word.length()) {
            if (!answer.contains(word)) {
                answer.add(word);
            }
            return;
        }

        int[][] direction = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        for (int i = 0; i < direction.length; i++) {
            int nextX = x + direction[i][0];
            int nextY = y + direction[i][1];
            if (nextX >= 0 && nextX < board.length && nextY >= 0 && nextY < board[0].length
                    && board[nextX][nextY] == word.charAt(charPointer) && visitCheck[nextX][nextY] == 0) {
                visitCheck[nextX][nextY] = 1;
                checkIfMatches(board, word, charPointer + 1, nextX, nextY, visitCheck);
                visitCheck[nextX][nextY] = 0;
            }
        }
    }
}
```

---

#### My logic & Feedback

The intention of the problem seems to be using 'Trie algorithm'.

And I realized it after I solved the problem by different approach, simple DFS, because people have uploaded their ideas in the discussion board and the most of them are Trie.

I have heard what Trie algorithm is, when I tried to solve a problem of some Korean algorithm website, but I failed to solve it by applying it.

I have totally forgotten learning the algorithm, so here I am not using it again..

My idea is, if a grid matches the first letter of any word of the input array words, it starts to search horizontal and vertical adjacent grids through recursive function to find the rest of characters until it is completed.

This approach is basically brute force, and the price of it is slowness..

If the time complexity constraint was tighter, my solution would not be able to pass this problem.

So I must learn this Trie algorithm.



