## Leetcode - Sum Root to Leaf Numbers [Medium]

Given a binary tree containing digits from `0-9` only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path `1->2->3` which represents the number `123`.

Find the total sum of all root-to-leaf numbers.

**Note:** A leaf is a node with no children.

**Example:**

```
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```

**Example 2:**

```
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```



Link : https://leetcode.com/problems/sum-root-to-leaf-numbers/

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
   int answer = 0;

    public int sumNumbers(TreeNode root) {
        recursion(root, new LinkedList<>());
        return answer;
    }

    public void recursion(TreeNode root, LinkedList<Integer> linkedList) {
        if (root == null) {
            return;
        } else {
            linkedList.add(root.val);
        }
        if (root.left == null && root.right == null) {
            StringBuilder sb = new StringBuilder();
            for (int each : linkedList) {
                sb.append("" + each);
            }
            answer += Integer.parseInt(sb.toString());
            return;
        }
        if (root.left != null) {
            recursion(root.left, linkedList);
            linkedList.removeLast();
        }
        if (root.right != null) {
            recursion(root.right, linkedList);
            linkedList.removeLast();
        }
    }
}

```

---



#### My logic & Feedback

별로 어렵지 않은 재귀문제다.

접근은 어렵지 않으나, 나는 코드를 깔끔하게 짜고싶다...