## Leetcode - Validate Binary Search Tree [Medium]

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

 

**Example 1:**

```
    2
   / \
  1   3

Input: [2,1,3]
Output: true
```

**Example 2:**

```
    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```



Link : https://leetcode.com/problems/validate-binary-search-tree/

---



#### My solution (Java)

```java
class Solution {
   int result = 0;

    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        recursion(root, Long.MIN_VALUE, Long.MAX_VALUE);
        if (result != 0) {
            return false;
        }
        return true;
    }

    public void recursion(TreeNode root, long leftLimit, long rightLimit) {
        if (root.left == null && root.right == null) {
            return;
        }

        if (root.left != null && root.left.val > leftLimit && root.left.val < root.val) {
            recursion(root.left, leftLimit, root.val);
        } else if (root.left != null && ((root.left.val <= leftLimit || root.left.val >= root.val))) {
            result++;
            return;
        }

        if (root.right != null && root.right.val < rightLimit && root.right.val > root.val) {
            recursion(root.right, root.val, rightLimit);
        } else if (root.right != null && ((root.right.val >= rightLimit || root.right.val <= root.val))) {
            result++;
            return;
        }
    }
}
```

---



#### My logic & Feedback

기본적인 BST 문제고, 재귀를 통해 간단히 해결가능한 문제다.

재귀를 사용하여 속도가 100%가 나왔는데,

코드가 길어져서 어떻게 하면 짧게 만들까 고민하다 discussion에서 놀라운 풀이를 봤다. 

풀이를 내 코드에 적용시켜서 코드를 짧게 만드니,

```
class Solution {
 public boolean isValidBST(TreeNode root) {
        return recursion(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public boolean recursion(TreeNode root, long leftLimit, long rightLimit) {
        if (root == null) {
            return true;
        }
        if (root.val >= rightLimit || root.val <= leftLimit) {
            return false;
        }
        return recursion(root.left, leftLimit, root.val) && recursion(root.right, root.val, rightLimit);
    }
}
```

과 같이 정리가 되었다.

재귀의 return값에 && 를 넣어서 표현하다니...소름이 돋는다.

코드 자체도 내 코드보다 훨씬 직관적이고 깔끔하다! 반드시 기억해놓자.