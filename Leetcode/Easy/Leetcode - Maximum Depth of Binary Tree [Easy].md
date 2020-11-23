## Leetcode - Maximum Depth of Binary Tree [Easy]

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Note:** A leaf is a node with no children.

**Example:**

Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its depth = 3.

Link : https://leetcode.com/problems/maximum-depth-of-binary-tree/



---



#### My solution (Java)

```java
def dfs(self, root, depth):
    if root : 
        return max(dfs(self, root.left, depth + 1), dfs(self, root.right, depth + 1))
    else : 
        return depth;


class Solution(object):
    def maxDepth(self, root):
        return dfs(self, root, 0)
        
```

---



#### My logic & Feedback

파이썬으로, 재귀로 풀었다.

BFS로 풀 수 있을거 같긴 한데, '깊이'를 묻는 문제이므로 그냥 직관적으로 dfs가 생각났고, 재귀로 풀었다.

구현하면서 재귀 코드를 최대한 깔끔하게 만드려고 노력했고, 상당히 클린한 코드를 쓴 것 같아 기분이 좋다.