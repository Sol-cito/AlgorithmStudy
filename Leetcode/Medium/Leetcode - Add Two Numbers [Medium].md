## Leetcode - Add Two Numbers [Medium]

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:**

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

Link : https://leetcode.com/problems/add-two-numbers/



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
        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode target1 = l1;
        ListNode target2 = l2;

        ListNode targetNode = new ListNode(0);
        ListNode firstNode = null;

        while (target1 != null || target2 != null) {
            if (target1 != null) {
                targetNode.val += target1.val;
                target1 = target1.next;
            }
            if (target2 != null) {
                targetNode.val += target2.val;
                target2 = target2.next;
            }
            if (firstNode == null) {
                firstNode = targetNode;
            }
            if (targetNode.val / 10 > 0 || (target1 != null || target2 != null)) {
                ListNode nextNode = new ListNode(targetNode.val / 10);
                targetNode.val = targetNode.val % 10;
                targetNode.next = nextNode;
                targetNode = nextNode;
            }
        }
        return firstNode;
    }
}
```

---



#### My logic & Feedback

쉬워 보이지만 풀이에 상당히 애를 먹었던 문제다..

처음 접근방식은, Nodelist에 있는 수를 모두 Stirng화하여 마지막에 Integer.parseInt 함수를 이용, integer로 바꾼 숫자를 다시 NodeList로 변환하여 return하려 했다.

그러나 테스트케이스에 Int는 커녕 Long 범위를 초과하는 숫자가 있었고(...)

위 풀이방식으로는 풀 수 없음을 알고 다른 방식으로 접근했다.

주어진 2개의 NodeList의 각각의 Node 숫자를 더해, element가 10 이상이면 그 다음 노드로 1을 주고(10으로 나눈 몫), 해당 노드에는 10으로 나눈 나머지 값을 부여한 후,

ListNode가 완성되면 가장 첫 번째 노드를 return하면 끝이다.

LeetCode는 프로그래머스와 달리 정답의 범위가 나타나있지 않아, 예상치못한 testCase를 마주하면 당황스럽다.