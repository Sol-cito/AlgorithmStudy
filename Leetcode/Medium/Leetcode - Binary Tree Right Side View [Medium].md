## Leetcode - Binary Tree Right Side View [Medium]

Given a binary tree, imagine yourself standing on the *right* side of it, return the values of the nodes you can see ordered from top to bottom.

**Example:**

```
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

Link : https://leetcode.com/problems/binary-tree-right-side-view/



---



#### My solution (Java)

```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
      List<Integer> answer = new ArrayList<>();
      if (root == null) {
          return answer;
      }
      Queue<TreeNode> que = new LinkedList<>();
      Queue<Integer> depthQue = new LinkedList<>();
          
      int depth = 1;
      que.add(root);
      depthQue.add(depth);
      answer.add(root.val);
        
      while (!que.isEmpty()) {
          TreeNode polled = que.poll();
          int polledDepth = depthQue.poll();
          if (polled.right != null) {
              que.add(polled.right);
              depthQue.add(polledDepth + 1);
          }
          if (polled.left != null) {
              que.add(polled.left);
              depthQue.add(polledDepth + 1);
          }
          if (polledDepth != depth) {
              depth = polledDepth;
              answer.add(polled.val);
          }
      }
      return answer;
  }
}
```

---

#### My logic & Feedback

각 노드의 Depth를 하나의 queue에 저장하고, 또 다른 queue에 노드를 저장하여 BFS로 풀면 되는 쉬운 문제다.

BFS로 왼쪽 노드부터 보면서 depth가 같은(같은 row에 위치한) 노드들 중 가장 오른쪽 노드(해당 depth의 마지막 노드)값을 

answer list에 저장하여 반환하면 끝.