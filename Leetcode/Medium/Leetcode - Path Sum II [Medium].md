## Leetcode - Path Sum II [Medium]

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

**Note:** A leaf is a node with no children.

**Example:**

Given the below binary tree and `sum = 22`,

```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
```

Return:

```
[
   [5,4,11,2],
   [5,8,4,5]
]
```



Link : https://leetcode.com/problems/path-sum-ii/

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
      List<List<Integer>> result = new LinkedList<>();

    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        if(root == null){
            return result;
        }
        recursive(root, sum, 0, new LinkedList<>());
        return result;
    }

    public void recursive(TreeNode root, int sum, int total, LinkedList<Integer> list) {
        if ((root.left == null && root.right == null)) {
            if (total + root.val == sum) {
                list.add(root.val);
                result.add(list);
            }
            return;
        }
        if (root.left != null) {
            list.add(root.val);
            recursive(root.left, sum, total + root.val, new LinkedList<>(list));
            list.removeLast();
        }
        if (root.right != null) {
            list.add(root.val);
            recursive(root.right, sum, total + root.val, new LinkedList<>(list));
            list.removeLast();
        }
    }
}
```

---



#### My logic & Feedback

문제에서 대놓고 재귀를 쓰라고 한다.

Binary Tree이므로 왼쪽, 오른쪽으로 재귀를 타면서 경로의 합을 구한 후,  sum과 같으면 return하면 끝이다.

근데 재귀로 하니 수행시간이 너무 느린데...뭔가 빠른방법이 있나 하고 discussion을 보니 거의 다 재귀로 풀었다. 더 빠르게 풀 수 있을거 같은데..