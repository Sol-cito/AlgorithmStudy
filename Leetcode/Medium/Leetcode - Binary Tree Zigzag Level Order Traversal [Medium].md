## Leetcode - Binary Tree Zigzag Level Order Traversal [Medium]

Given a binary tree, return the *zigzag level order* traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```



return its zigzag level order traversal as:

```
[
  [3],
  [20,9],
  [15,7]
]
```



Link : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

---



#### My solution (Java)

```java
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> answerList = new ArrayList<>();
        if (root == null) {
            return answerList;
        }
        Queue<TreeNode> que = new LinkedList<>();
        int direction = 1;
        que.add(root);

        Queue<Integer> depthQue = new LinkedList<>();
        depthQue.add(0);

        LinkedList<Integer> list = new LinkedList<>();
        int depth = 0;

        while (!que.isEmpty()) {
            TreeNode polled = que.poll();
            int polledDepth = depthQue.poll();
            if (polledDepth != depth) {
                answerList.add(list);
                list = new LinkedList<>();
                depth = polledDepth;
                direction = switchDirection(direction);
            }
            if (direction == 0) {
                list.addFirst(polled.val);
            } else {
                list.addLast(polled.val);
            }
            if (polled.left != null) {
                que.add(polled.left);
                depthQue.add(polledDepth + 1);
            }
            if (polled.right != null) {
                que.add(polled.right);
                depthQue.add(polledDepth + 1);
            }
        }
        answerList.add(list);
        return answerList;
    }

    public int switchDirection(int target) {
        if (target == 0) {
            return 1;
        }
        return 0;
    }
}
```

---



#### My logic & Feedback

https://leetcode.com/problems/binary-tree-level-order-traversal/ 

위 문제와 거의 유사하나 '방향'이 존재한다는 점이 다르다.

처음엔 Deque를 써보려 했으나 잘 안되었고, 그냥 LinkedList의 addFirst와 addLast를 이용하여 list에 넣는 방향을 달리해 간단히 풀었다.