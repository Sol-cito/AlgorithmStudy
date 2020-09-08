## Leetcode - Swap Nodes in Pairs [Medium]

Given a linked list, swap every two adjacent nodes and return its head.

You may **not** modify the values in the list's nodes, only nodes itself may be changed.

 

**Example:**

```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```



Link : https://leetcode.com/problems/swap-nodes-in-pairs/

---



#### My solution (Java)

```java
import java.util.ArrayList;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
   public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        int cnt = 0;
        ListNode returnNode = head.next;
        ListNode previousNode = null;
        ListNode targetNode = head;
        while (targetNode != null && targetNode.next != null) {
            if (cnt % 2 == 0) {
                if (cnt > 0) {
                    previousNode.next = targetNode.next;
                }
                ListNode nextNextNode = targetNode.next.next;
                targetNode.next.next = targetNode;
                targetNode.next = nextNextNode;
                previousNode = targetNode;
                targetNode = nextNextNode;
            }
            cnt++;
        }
        return returnNode;
    }
}
```

---



#### My logic & Feedback

속도가 0ms가 나왔다. 그도 그럴것이, 시간복잡도가 O(n/2) 가 되도록 코드를 짰기 때문이다. 

물론 그 과정이 시행착오를 반복하며 오래걸리긴 했지만..

Leetcode에서 자주 등장하는 위와 같은 ListNode 류의 문제는 index가 없다는 것이 어려운 점이다.

사실 문제를 편하게 풀려면 O(N)으로 한바퀴를 돌면서 HashMap에 각 Node를 저장하면 index를 부여한것과 같은 효과를 얻을 수 있다.

그러나 Map을 이용하는 순간 속도와 메모리를 내주어야 하는 단점이 존재..그래서 오기가 생겨 map을 안쓰고 푸는 방법을 생각했다.

사실 풀이 자체는 간단하다. 2개의 노드를 서로 바꾸어주면 되므로, 짝수번째 노드만 신경쓰면 된다.

짝수번째 노드일 때, 현재노드(targetNode), 현재 노드.next, 현재노드.next.next 를 잘 생각해서 서로서로 스왑해주면 된다.

보기엔 간단해 보이지만, 구현하는데 자꾸 헷갈려서 생각보다 시간이 좀 걸렸다.