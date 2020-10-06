## Leetcode - Simplify Path [Medium]

Given an **absolute path** for a file (Unix-style), simplify it. Or in other words, convert it to the **canonical path**.

In a UNIX-style file system, a period `.` refers to the current directory. Furthermore, a double period `..` moves the directory up a level.

Note that the returned canonical path must always begin with a slash `/`, and there must be only a single slash `/` between two directory names. The last directory name (if it exists) **must not** end with a trailing `/`. Also, the canonical path must be the **shortest** string representing the absolute path.

 

**Example 1:**

```
Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
```

**Example 2:**

```
Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
```

**Example 3:**

```
Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
```

**Example 4:**

```
Input: "/a/./b/../../c/"
Output: "/c"
```

**Example 5:**

```
Input: "/a/../../b/../c//.//"
Output: "/c"
```

**Example 6:**

```
Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
```

Link : https://leetcode.com/problems/simplify-path/

---



#### My solution (Java)

```java
class Solution {
    public String simplifyPath(String path) {
        StringBuilder sb = new StringBuilder();
        LinkedList<String> linkedList = new LinkedList<>();
        String[] split = path.split("/");
        for (String element : split) {
            if (element.length() > 0 && !element.equals(".") && !element.equals("..")) {
                linkedList.add(element);
            } else if (element.equals("..") && linkedList.size() > 0) {
                linkedList.removeLast();
            }
        }
        for (int i = 0; i < linkedList.size(); i++) {
            sb.append("/").append(linkedList.get(i));
        }
        return sb.length() == 0 ? "/" : sb.toString();
    }
}

```

---



#### My logic & Feedback

문제에 싫어요가 좋아요의 2배가 넘던데, 왤까? 그렇게 짜증나는 문제는 아닌데...

딱-봐도 stack이나 queue같은 자료구조를 쓰는 유형의 문제인데, 나는 그냥 직관적으로 linkedList를 썼다.

split으로 자른 다음, ~~한 조건에서는 linkedlist에 element를 붙이고, ~~한 조건에서는 remove하는 식으로..

이 문제를 풀면서 ArrayList와 LinkedList의 차이에 대해서 조금 살펴보았는데,

element를 추가, 삭제할 때는 당연히 linkedList가 빠르다. 

추가할 때는 앞 뒤 노드에 새로운 주소값을 씌우고 새로운 노드에 앞 뒤 노드의 주소값을 저장만 하면 되고,

삭제를 할 때는 다음 노드의 주소값만 제거해주면 연결이 끊어지기 때문이다(시간복잡도 O(1)).

반면 배열 기반으로 이루어진 ArrayList의 경우,

새 data가 ''중간''에 추가되거나 삭제될 경우, **data를 새로운 배열에 통째로 복사**해야되기 때문에 당연히 시간복잡도가 O(N)이 된다.

배열을 기반으로 한 ArrayList의 장점은 index를 가지고있다는 점이다. 

따라서 .get(i) 메소드의 경우 LinkedList보다 ArrayList가 훨씬 빠르다.

탐색의 경우 ArrayList의 시간복잡도는 O(1), LinkedList는 최악의 경우 O(N)이다.

따라서 주어진 문제의 성격을 잘 파악해서, 탐색과 삭제의 기능 중 무엇에 우위를 둘 것인지,

어떤 자료구조를 선택하여 성능좋은 알고리즘을 짤 것인지 고민해보아야 한다.