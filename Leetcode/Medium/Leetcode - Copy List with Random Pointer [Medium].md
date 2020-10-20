## Leetcode - Copy List with Random Pointer [Medium]

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of the list.

The Linked List is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

- `val`: an integer representing `Node.val`
- `random_index`: the index of the node (range from `0` to `n-1`) where random pointer points to, or `null` if it does not point to any node.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2019/12/18/e1.png)

```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2019/12/18/e2.png)

```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

**Example 3:**

**![img](https://assets.leetcode.com/uploads/2019/12/18/e3.png)**

```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

**Example 4:**

```
Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
```

 

**Constraints:**

- `-10000 <= Node.val <= 10000`
- `Node.random` is null or pointing to a node in the linked list.
- The number of nodes will not exceed 1000.

Link : https://leetcode.com/problems/copy-list-with-random-pointer/submissions/

---



#### My solution (Java)

```java
/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/
class Solution {
   public Node copyRandomList(Node head) {
        if (head == null) return null;
        HashMap<Node, Node> map = new HashMap<>();
        Node target = head;
        Node pre = null;
        while (target != null) {
            map.put(target, new Node(target.val));
            if (pre != null) {
                pre.next = map.get(target);
            }
            pre = map.get(target);
            target = target.next;
        }
        target = head;
        while (target != null) {
            if (target.random == null) {
                map.get(target).random = null;
            } else {
                map.get(target).random = map.get(target.random);
            }
            target = target.next;
        }
        return map.get(head);
    }
}
```

---



#### My logic & Feedback

갓시맵을 사용하여 O(N)으로 풀 수 있는 문제다.

HashMap을 사용하면 풀이 자체는 매우 쉽다. 그러나 내가 이 문제를 통해 하나 얻은것은,

HashMap의 Key로 Object가 올 수도 있다는 것이다!

정확하게 말하면, 객체 instance가 저장된 **스택 주소값**을 Map의 Key로 세팅할 수 있다는 것이다.

문제는 Deep Copy를 요구하므로, 기존의 Node를 Key로 하는 Map을 설정하기 위해 while 한바퀴를 돌고,

Copy해놓은 Node의 Random을 설정하기 위한 while을 한 바퀴 돌면서 Map을 이용하면 쉽게 풀린다!

위 풀이로 속도는 100%가 나왔다. 물론 Map을 썼기 때문에 메모리 누수가 좀 있었지만...