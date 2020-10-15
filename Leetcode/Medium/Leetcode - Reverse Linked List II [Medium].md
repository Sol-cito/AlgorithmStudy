## Leetcode - Reverse Linked List II [Medium]

- reverse a linked list from position *m* to *n*. Do it in one-pass.

  **Note:** 1 ≤ *m* ≤ *n* ≤ length of list.

  **Example:**

  ```
  Input: 1->2->3->4->5->NULL, m = 2, n = 4
  Output: 1->4->3->2->5->NULL
  ```

- Link : https://leetcode.com/problems/reverse-linked-list-ii/

---



#### My solution (Java)

```java
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ArrayList<ListNode> list = new ArrayList<>();
        int cnt = 0;
        int listIndex = 0;
        ListNode target = head;
        while (cnt < n) {
            if (cnt < (m + n) / 2) {
                list.add(target);
                listIndex = list.size() - 1;
            } else {
                int temp = target.val;
                target.val = list.get(listIndex - (m + n + 1) % 2).val;
                list.get(listIndex - (m + n + 1) % 2).val = temp;
                listIndex--;
            }
            cnt++;
            target = target.next;
        }
        return head;
    }
}
```

---



#### My logic & Feedback

인덱스 때문에 머리가 좀 아팠다...

기본 idea는, m에 도달할 때까지 list에 ListNode를 담는다(문제에 메모리 제한이 없으므로).

그리고 다시 n에 도달할 때까지 list에 담긴 node를 거꾸로 탐색하면서 현재 노드와 값을 바꾼다.

단, m과 n의 합이 짝수일 때와 홀수일 때 index가 달라질 수 있어서, 그 처리에만 주의하면 쉽게 풀린다.

위 코드는 속도는 100%이나 list의 사용으로 인해 메모리는 별로 효율이 좋지 못한 풀이법이다.