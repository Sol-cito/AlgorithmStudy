## Leetcode - Rotate List [Medium]

- Given a linked list, rotate the list to the right by *k* places, where *k* is non-negative.

  **Example 1:**

  ```
  Input: 1->2->3->4->5->NULL, k = 2
  Output: 4->5->1->2->3->NULL
  Explanation:
  rotate 1 steps to the right: 5->1->2->3->4->NULL
  rotate 2 steps to the right: 4->5->1->2->3->NULL
  ```

  **Example 2:**

  ```
  Input: 0->1->2->NULL, k = 4
  Output: 2->0->1->NULL
  Explanation:
  rotate 1 steps to the right: 2->0->1->NULL
  rotate 2 steps to the right: 1->2->0->NULL
  rotate 3 steps to the right: 0->1->2->NULL
  rotate 4 steps to the right: 2->0->1->NULL
  ```

Link : https://leetcode.com/problems/rotate-list/



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
       public ListNode rotateRight(ListNode head, int k) {
        ListNode newHead = head;
        int totalNum = 0;
        HashMap<Integer, ListNode> map = new HashMap<>();
        int mapIndex = 0;
        ListNode target = head;
        while (target != null) {
            map.put(mapIndex, target);
            totalNum++;
            mapIndex++;
            target = target.next;
        }
        if(totalNum == 0){
            return head;
        }
        int nextIndex = 0;
        for (int i = 1; i <= k % totalNum; i++) {
            map.get(totalNum - i).next = map.get(nextIndex);
            nextIndex = totalNum - i;
            map.get(totalNum - i - 1).next = null;
            newHead = map.get(totalNum - i);
        }
        return newHead;
    }
}
```

---



#### My logic & Feedback

ListNode의 맨 끝 node의 next를 null에서 가장 첫 번째 node로 바꾸고,

맨 끝에서 앞의 node의 next를 null로 k번 바꿔주기만 하면 된다.

Rotation이라는 조건의 특성상 k%(노드의 총 개수) 로 loop숫자를 줄였으며,

HashMap을 사용해 next를 변경해줄 노드를 바로바로 찾을 수 있도록 구현하였다.