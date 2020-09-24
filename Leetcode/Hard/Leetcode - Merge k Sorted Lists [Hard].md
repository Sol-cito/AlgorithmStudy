## Leetcode - Merge k Sorted Lists [Hard]

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

 

**Example 1:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

**Example 2:**

```
Input: lists = []
Output: []
```

**Example 3:**

```
Input: lists = [[]]
Output: []
```

 

**Constraints:**

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in **ascending order**.
- The sum of `lists[i].length` won't exceed `10^4`.

Link : https://leetcode.com/problems/n-queens/



---

#### My solution 1 (Java) - standard switching nodes

```java
class Solution {
     public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }
        ListNode firstNode = null;
        ListNode smallestNode = null;
        ListNode targetNode = new ListNode();

        while (targetNode != null) {
            smallestNode = null;
            int smallestIndex = 0;
            for (int i = 0; i < lists.length; i++) {
                if ((lists[i] != null && smallestNode == null) || (lists[i] != null && smallestNode.val >= lists[i].val)) {
                    smallestNode = lists[i];
                    smallestIndex = i;
                }
            }
            if (firstNode == null) {
                firstNode = smallestNode;
                targetNode = firstNode;
            } else {
                targetNode.next = smallestNode;
                targetNode = targetNode.next;
            }
            if (lists[smallestIndex] != null) {
                lists[smallestIndex] = lists[smallestIndex].next;
            }
        }
        return firstNode;
    }
}
```

---

#### My solution 2 (Java) - using Collection.sort

```
class Solution {
     public ListNode mergeKLists(ListNode[] lists) {
        ArrayList<Integer> numList = new ArrayList<>();
        for (int i = 0; i < lists.length; i++) {
            ListNode node = lists[i];
            while (node != null) {
                numList.add(node.val);
                node = node.next;
            }
        }
        Collections.sort(numList);
        ListNode firstNode = null;
        ListNode targetNode = null;
        for (int i = 0; i < numList.size(); i++) {
            if (firstNode == null) {
                firstNode = new ListNode(numList.get(i));
                targetNode = firstNode;
            } else {
                targetNode.next = new ListNode(numList.get(i));
                targetNode = targetNode.next;
            }
        }
        return firstNode;
    }
}
```



---

#### My solution 3 (Java) - using Priority Queue

```
class Solution {
   public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>(new Comparator<ListNode>() {
            @Override
            public int compare(ListNode o1, ListNode o2) {
                return o1.val - o2.val;
            }
        });
        for (int i = 0; i < lists.length; i++) {
            ListNode node = lists[i];
            while (node != null) {
                pq.add(node);
                node = node.next;
            }
        }
        ListNode firstNode = null;
        ListNode targetNode = null;

        while (!pq.isEmpty()) {
            ListNode polled = pq.poll();
            if (firstNode == null) {
                firstNode = polled;
                targetNode = firstNode;
            } else {
                targetNode.next = polled;
                targetNode = targetNode.next;
                if (pq.size() == 0) {
                    targetNode.next = null;
                }
            }
        }
        return firstNode;
    }
}
```

---

#### My logic & Feedback

There are various ways to solve this problem. 

My first approach was just to keep switching nodes by comparing their values, but it is quite slow since searching the list should be done every time of which time complexity is O(N^2). Yet it consumes the least memory among these three solutions.

Second one is quite simple. All I have to do is just to insert each node value into an array list, sort it, and lastly 'create' new list nodes with each value element of the array list.

It is very easy idea to come up with, but needs more memory usage than the first one because it uses an array list and creates new list node objects.

The last one is basically similar to the second idea, but priority queue makes it faster than Collection.sort method.

It also occupies more memory space than the first one, obviously.



