## Leetcode - Partition List [Medium]

Given a linked list and a value *x*, partition it such that all nodes less than *x* come before nodes greater than or equal to *x*.

You should preserve the original relative order of the nodes in each of the two partitions.

**Example:**

```
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
```

Link : https://leetcode.com/problems/partition-list/



---



#### My solution (Java)

```java
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
    public ListNode partition(ListNode head, int x) {
        if(head == null){
            return null;
        }
        LinkedList<ListNode> linkedList = new LinkedList<>();
        int addIndex = 0;

        ListNode targetNode = head;
        while (targetNode != null) {
            if (targetNode.val < x) {
                linkedList.add(addIndex, targetNode);
                addIndex++;
            } else {
                linkedList.addLast(targetNode);
            }
            targetNode = targetNode.next;
        }
        for (int i = 0; i < linkedList.size() - 1; i++) {
            linkedList.get(i).next = linkedList.get(i + 1);
        }
        linkedList.get(linkedList.size() - 1).next = null;
        return linkedList.get(0);
    }
}
```

---



#### My logic & Feedback

여러가지 방법이 있으나, linkedList가 가장 깔끔하게 풀 수 있는 방법이라 생각하고 LinkedList를 활용하였다.

LinkedList의 특성상 index를 지정하여 add를 하면 양쪽 node의 index가 저절로 조절이 되기 때문이다.

따라서 x값보다 작은 수들은 index를 적절히 활용하여 중간에 넣어주고, x값보다 큰 수들은 addLast를 통하여 끝에 붙여가가면 된다.

최종적으로 만들어진 linkedList의 각 element의 next를 다음번 element로 지정해주면 끝.