## Leetcode - Clone Graph [Medium]

Given a reference of a node in a **[connected](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph)** undirected graph.

Return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph.

Each node in the graph contains a val (`int`) and a list (`List[Node]`) of its neighbors.

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```

 

**Test case format:**

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with `val = 1`, the second node with `val = 2`, and so on. The graph is represented in the test case using an adjacency list.

**Adjacency list** is a collection of unordered **lists** used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the **copy of the given node** as a reference to the cloned graph.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png)

```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2020/01/07/graph.png)

```
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
```

**Example 3:**

```
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
```

**Example 4:**

![img](https://assets.leetcode.com/uploads/2020/01/07/graph-1.png)

```
Input: adjList = [[2],[1]]
Output: [[2],[1]]
```

 

**Constraints:**

- `1 <= Node.val <= 100`
- `Node.val` is unique for each node.
- Number of Nodes will not exceed 100.
- There is no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

Link : https://leetcode.com/problems/clone-graph/



---



#### My solution (Java)

```java
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
   public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }
        Queue<Node> que = new LinkedList<>();
        que.add(node);
        HashMap<Integer, Node> map = new HashMap<>();
        while (!que.isEmpty()) {
            Node polled = que.poll();
            Node newNode = null;
            if (map.get(polled.val) == null) {
                newNode = new Node(polled.val, new ArrayList<>());
                map.put(polled.val, newNode);
            } else {
                newNode = map.get(polled.val);
            }
            for (Node element : polled.neighbors) {
                if (!map.containsKey(element.val)) {
                    que.add(element);
                }
                if (map.get(element.val) == null) {
                    Node eleNode = new Node(element.val, new ArrayList<>());
                    newNode.neighbors.add(eleNode);
                    map.put(element.val, eleNode);
                } else {
                    newNode.neighbors.add(map.get(element.val));
                }
            }
        }
        return map.get(1);
    }
}

```

---



#### My logic & Feedback

Node Graph 의 깊은 복사 구현 문제로, Node 인스턴스 내부의 ArrayList를 복사하는 것이 문제의 핵심이다.

HashMap을 이용하면 효율적으로 해결할 수 있다.

이미 map에 담긴 Node라면 복사한 Node까리 연결을, 아니라면 Node를 새로 Copy한 후 담아주면 된다.

위 코드는 속도, 메모리 모두 90%를 넘은 코드다. 다른 사람들도 대부분 HashMap을 이용해서 문제를 푼 것 같다.

아, HashMap에는 containKeys() 라는 메소드가 있는데, 저장되어있는 Key값이 있는지 확인해주는 메소드다.

이 메소드는 visitcheck가 필요할 때 활용 가능하니, 잘 기억해두도록 하자.

