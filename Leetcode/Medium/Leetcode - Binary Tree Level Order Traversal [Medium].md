## Leetcode - Binary Tree Level Order Traversal [Medium]

Given a binary tree, return the *level order* traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```



return its level order traversal as:

```
[
  [3],
  [9,20],
  [15,7]
]
```



Link : https://leetcode.com/problems/binary-tree-level-order-traversal/

---



#### My solution (Java)

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
  public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> answer = new ArrayList<>();
        if (root == null) {
            return answer;
        }
        Queue<TreeNode> que = new LinkedList<>();
        Queue<Integer> depthQue = new LinkedList<>();
        que.add(root);
        int targetDepth = 1;
        depthQue.add(1);
        List<Integer> list = new ArrayList<>();
        while (!que.isEmpty()) {
            TreeNode polledTreeNode = que.poll();
            int polledDepth = depthQue.poll();
            if (polledDepth == targetDepth) {
                list.add(polledTreeNode.val);
            } else {
                answer.add(list);
                list = new ArrayList<>();
                list.add(polledTreeNode.val);
                targetDepth = polledDepth;
            }
            if (polledTreeNode.left != null) {
                que.add(polledTreeNode.left);
                depthQue.add(polledDepth + 1);
            }
            if (polledTreeNode.right != null) {
                que.add(polledTreeNode.right);
                depthQue.add(polledDepth + 1);
            }
        }
        answer.add(list);
        return answer;
    }
}
```

---



#### My logic & Feedback

Queue와 Depth를 이용해서 풀 수 있는 문제다.

재귀로도 풀 수 있을 것 같은데, queue가 더 간단하고 빨라보여 queue로 구현했다.

그러나 풀이 시간이 그렇게 만족스럽게 나오지는 않았다.