## Leetcode - Lowest Common Ancestor of a Binary Tree [Medium]

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

**Example 3:**

```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

 

**Constraints:**

- The number of nodes in the tree is in the range `[2, 105]`.
- `-109 <= Node.val <= 109`
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the tree.

Link : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/



---

#### My solution (Java)

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        Queue<TreeNode> que = new LinkedList<>();
        HashMap<TreeNode, TreeNode> map = new HashMap<>(); // node, its root node
        que.add(root);
        while (!que.isEmpty()) {
            TreeNode polled = que.poll();
            if (polled.left != null) {
                que.add(polled.left);
                map.put(polled.left, polled);
            }
            if (polled.right != null) {
                que.add(polled.right);
                map.put(polled.right, polled);
            }
        }
        Set<TreeNode> set = new HashSet<>();
        while (p != null) {
            set.add(p);
            p = map.get(p);
        }
        while (q != null) {
            if (set.contains(q)) {
                return q;
            }
            q = map.get(q);
        }
        return null;
    }
}

```

---



#### My logic & Feedback

음..풀이방법 구상 자체는 쉬웠는데, 생각보다 속도가 낮다.

접근방법은, 우선 BFS로 노드 전체를 level 순회하는데, 순회하면서 HashMap에 <노드, 해당 노드의 parent 노드>를 담는다.

그 다음 HashMap을 이용, p노드와 q노드에서부터 출발하여 root까지 가는데, 

set자료구조를 이용하여 두 노드가 root까지 가는 도중 만나는 최초의 TreeNode를 반환한다.

따라서 본 풀이법은 O(N) 풀이법인데, 최악의 경우(q노드가 root이고 p노드가 leaf 노드일 경우) 3 * O(N)의 시간복잡도를 갖는다.

뭔가 p와 q 노드가 파라미터로 주어지기 때문에 더 빠른 풀이법이 있을 것 같는 느낌이다.