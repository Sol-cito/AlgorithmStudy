## Leetcode - Remove Duplicates from Sorted List II [Medium]

- Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only *distinct* numbers from the original list.

  Return the linked list sorted as well.

  **Example 1:**

  ```
  Input: 1->2->3->3->4->4->5
  Output: 1->2->5
  ```

  **Example 2:**

  ```
  Input: 1->1->1->2->3
  Output: 2->3
  ```

Link : https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/



---



#### My solution (Java)

```java
class Solution {
     public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }
        HashMap<Integer, Integer> map = new HashMap<>();
        ListNode targetNode = head;
        while (targetNode != null) {
            if (map.get(targetNode.val) == null) {
                map.put(targetNode.val, 1);
            } else {
                map.replace(targetNode.val, map.get(targetNode.val) + 1);
            }
            targetNode = targetNode.next;
        }
        ListNode returnNode = null;
        ListNode previousNode = null;
        targetNode = head;
        while (targetNode != null) {
            if (map.get(targetNode.val) == 1) {
                if (returnNode == null) {
                    returnNode = targetNode;
                } else {
                    previousNode.next = targetNode;
                }
                previousNode = targetNode;
            }
            targetNode = targetNode.next;
        }
        if (returnNode != null) {
            previousNode.next = null;
        }
        return returnNode;
    }
}
```

---



#### My logic & Feedback

Easy to solve by using HashMap, but not the best solution since it is two passes code. 

Once to store keys and values in the map, and one more to verify which nodes should be filtered for having duplicate numbers.

I think there must be one pass solution but I was too tired solving four algorithm problems a day so just took the easiest path..

