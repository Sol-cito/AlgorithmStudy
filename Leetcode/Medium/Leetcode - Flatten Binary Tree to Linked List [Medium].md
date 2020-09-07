## Leetcode - Flatten Binary Tree to Linked List [Medium]

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

```
    1
   / \
  2   5
 / \   \
3   4   6
```

The flattened tree should look like:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```



Link : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

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
      public void flatten(TreeNode root) {
         if (root == null) {
            return;
        }
        Stack<TreeNode> stack = new Stack<>();
        stack.add(root);
        while (!stack.isEmpty()) {
            TreeNode target = stack.pop();
            if (target.right != null) {
                stack.add(target.right);
            }
            if (target.left != null) {
                stack.add(target.left);
            }
            if (!stack.isEmpty() && stack.peek() != null) {
                target.right = stack.peek();
                target.left = null;
            }
        }
    }
}
```

---



#### My logic & Feedback

간단히 stack으로 구현했다. 어려운 문제는 아닌데...

Discussion 게시판을 보니 엄청나게 짧고 효율적으로 재귀로 푼 사람이 있어 링크를 첨부한다;

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36977/My-short-post-order-traversal-Java-solution-for-share

경이롭다..