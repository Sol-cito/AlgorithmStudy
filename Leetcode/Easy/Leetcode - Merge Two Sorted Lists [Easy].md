## Leetcode - Merge Two Sorted Lists [Easy]

Merge two sorted linked lists and return it as a new **sorted** list. The new list should be made by splicing together the nodes of the first two lists.

**Example:**

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

Link : https://leetcode.com/problems/merge-two-sorted-lists/



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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ArrayList<Integer> list = new ArrayList<>();
        while (l1 != null || l2 != null) {
            if (l1 != null) {
                list.add(l1.val);
                l1 = l1.next;
            }
            if (l2 != null) {
                list.add(l2.val);
                l2 = l2.next;
            }
        }
        Collections.sort(list);
        ListNode firstNode = null;
        ListNode listNode = new ListNode();
        for (int i : list) {
            ListNode nextNode = new ListNode();
            if (firstNode == null) {
                firstNode = new ListNode(i);
                listNode = firstNode;
            } else {
                nextNode.val = i;
                listNode.next = nextNode;
                listNode = nextNode;
            }
        }
        return firstNode;
    }
}
```

---



#### My logic & Feedback

정석대로 풀려면 양쪽 list를 pointer 등을 통해 값을 왔다갔다 비교하면서 merge해주면 되지만...

귀찮아서 쉬운 방법을 택했다(하지만 느리다).

ArrayList에 두 노드의 값을 모두 담은 후 정렬시킨다.

그리고 ArrayList의 값을 새로운 ListNode에 담으면 끝.

이 방법이 느린 이유는, 우선 ArrayList라는 객체를 만들어 O(n) 만큼 탐색 + 정렬 시간 + 다시 ArrayList 탐색 O(n) 이기 때문이다.

만약 Pointer를 써서 양쪽 노드를 동시에 보면서 값을 비교하여 바로 ListNode에 담으면 O(n) 만에 해결할 수 있다.

그러나 귀찮아서...