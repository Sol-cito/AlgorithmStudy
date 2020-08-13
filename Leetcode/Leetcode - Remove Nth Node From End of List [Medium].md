## Leetcode - Remove Nth Node From End of List [Medium]

Given a linked list, remove the *n*-th node from the end of list and return its head.

**Example:**

```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```

**Note:**

Given *n* will always be valid.

Link : https://leetcode.com/problems/remove-nth-node-from-end-of-list/



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
        public ListNode removeNthFromEnd(ListNode head, int n) {
            HashMap<Integer, ListNode> map = new HashMap<>();
            ListNode target = head;
            int count = 1;
            while (target != null) {
                map.put(count, target);
                target = target.next;
                count++;
            }
            if (count - 1 == n) {
                head = map.get(count - n + 1);
            } else {
                map.get(count - n - 1).next = map.get(count - n + 1);
            }
            return head;
        }
    }
```

---



#### My logic & Feedback

The point of this question is, I guess, to see if the participant knows the concept of linked list.

It's chained to each other by pointing next node's memory address,

and here in this question, the 'List node' of which concept is basically the same shows up on the field.

All I had to do was just to find nth node from the back by using count variable, 

and at the same time to store each node in Hash map to find which node should be removed and which to relink.

