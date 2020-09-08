## Leetcode - Reorder List [Medium]

Given a singly linked list *L*: *L*0→*L*1→…→*L**n*-1→*L*n,
reorder it to: *L*0→*L**n*→*L*1→*L**n*-1→*L*2→*L**n*-2→…

You may **not** modify the values in the list's nodes, only nodes itself may be changed.

**Example 1:**

```
Given 1->2->3->4, reorder it to 1->4->2->3.
```

**Example 2:**

```
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```

Link : https://leetcode.com/problems/reorder-list/

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
  public void reorderList(ListNode head) {
        if (head == null) {
            return;
        }
        HashMap<Integer, ListNode> map = new HashMap<>();
        int cnt = 0;
        while (head != null) {
            map.put(cnt, head);
            head = head.next;
            cnt++;
        }
        int count = 0;
        int firstIndex = 1;
        int lastIndex = cnt - 1;
        ListNode target = map.get(0);
        while (count < cnt) {
            if (count % 2 == 0) {
                target.next = map.get(lastIndex);
                lastIndex--;
            } else {
                target.next = map.get(firstIndex);
                firstIndex++;
            }
            target = target.next;
            count++;
            if (count == cnt) {
                target.next = null;
            }
        }
    }
}
```

---



#### My logic & Feedback

이 문제는 맨 처음 node와 맨 끝 node를 swap해주는거라...우선 처음에 한 바퀴를 돌지 않으면 안되었다.

그래서 그냥 O(N)의 시간복잡도 및 메모리를 희생하여 map에 순서대로 list를 담은 후,

key값을 이리저리 조작하여 swap을 해주었다.

예상대로 풀이속도 및 메모리가 썩 만족스럽지는 못했는데, 어떻게 하면 더 빠른 속도를 낼 수 있을까?