## 프로그래머스 길 찾기 게임 (Level 3)

###### 문제 설명

## 길 찾기 게임

전무로 승진한 라이언은 기분이 너무 좋아 프렌즈를 이끌고 특별 휴가를 가기로 했다.
내친김에 여행 계획까지 구상하던 라이언은 재미있는 게임을 생각해냈고 역시 전무로 승진할만한 인재라고 스스로에게 감탄했다.

라이언이 구상한(그리고 아마도 라이언만 즐거울만한) 게임은, 카카오 프렌즈를 두 팀으로 나누고, 각 팀이 같은 곳을 다른 순서로 방문하도록 해서 먼저 순회를 마친 팀이 승리하는 것이다.

그냥 지도를 주고 게임을 시작하면 재미가 덜해지므로, 라이언은 방문할 곳의 2차원 좌표 값을 구하고 각 장소를 이진트리의 노드가 되도록 구성한 후, 순회 방법을 힌트로 주어 각 팀이 스스로 경로를 찾도록 할 계획이다.

라이언은 아래와 같은 특별한 규칙으로 트리 노드들을 구성한다.

- 트리를 구성하는 모든 노드의 x, y 좌표 값은 정수이다.
- 모든 노드는 서로 다른 x값을 가진다.
- 같은 레벨(level)에 있는 노드는 같은 y 좌표를 가진다.
- 자식 노드의 y 값은 항상 부모 노드보다 작다.
- 임의의 노드 V의 왼쪽 서브 트리(left subtree)에 있는 모든 노드의 x값은 V의 x값보다 작다.
- 임의의 노드 V의 오른쪽 서브 트리(right subtree)에 있는 모든 노드의 x값은 V의 x값보다 크다.

아래 예시를 확인해보자.

라이언의 규칙에 맞게 이진트리의 노드만 좌표 평면에 그리면 다음과 같다. (이진트리의 각 노드에는 1부터 N까지 순서대로 번호가 붙어있다.)

![tree_3.png](https://grepp-programmers.s3.amazonaws.com/files/production/dbb58728bd/a5371669-54d4-42a1-9e5e-7466f2d7b683.jpg)

이제, 노드를 잇는 간선(edge)을 모두 그리면 아래와 같은 모양이 된다.

![tree_4.png](https://grepp-programmers.s3.amazonaws.com/files/production/6bd8f6496a/50e1df20-5cb7-4846-86d6-2a2f1e70c5da.jpg)

위 이진트리에서 전위 순회(preorder), 후위 순회(postorder)를 한 결과는 다음과 같고, 이것은 각 팀이 방문해야 할 순서를 의미한다.

- 전위 순회 : 7, 4, 6, 9, 1, 8, 5, 2, 3
- 후위 순회 : 9, 6, 5, 8, 1, 4, 3, 2, 7

다행히 두 팀 모두 머리를 모아 분석한 끝에 라이언의 의도를 간신히 알아차렸다.

그러나 여전히 문제는 남아있다. 노드의 수가 예시처럼 적다면 쉽게 해결할 수 있겠지만, 예상대로 라이언은 그렇게 할 생각이 전혀 없었다.

이제 당신이 나설 때가 되었다.

곤경에 빠진 카카오 프렌즈를 위해 이진트리를 구성하는 노드들의 좌표가 담긴 배열 nodeinfo가 매개변수로 주어질 때,
노드들로 구성된 이진트리를 전위 순회, 후위 순회한 결과를 2차원 배열에 순서대로 담아 return 하도록 solution 함수를 완성하자.

##### 제한사항

- nodeinfo는 이진트리를 구성하는 각 노드의 좌표가 1번 노드부터 순서대로 들어있는 2차원 배열이다.
  - nodeinfo의 길이는 `1` 이상 `10,000` 이하이다.
  - nodeinfo[i] 는 i + 1번 노드의 좌표이며, [x축 좌표, y축 좌표] 순으로 들어있다.
  - 모든 노드의 좌표 값은 `0` 이상 `100,000` 이하인 정수이다.
  - 트리의 깊이가 `1,000` 이하인 경우만 입력으로 주어진다.
  - 모든 노드의 좌표는 문제에 주어진 규칙을 따르며, 잘못된 노드 위치가 주어지는 경우는 없다.

------

##### 입출력 예

| nodeinfo                                                  | result                                    |
| --------------------------------------------------------- | ----------------------------------------- |
| [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]] | [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]] |

##### 입출력 예 설명

입출력 예 #1

문제에 주어진 예시와 같다.



출처 : https://programmers.co.kr/learn/courses/30/lessons/42892



---



#### My solution (Java)

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

class Solution {
  public int[][] solution(int[][] nodeinfo) {
        TreeNode[] nodeArr = new TreeNode[nodeinfo.length];
        for (int i = 0; i < nodeinfo.length; i++) {
            TreeNode treeNode = new TreeNode(i + 1, nodeinfo[i][0], nodeinfo[i][1]);
            nodeArr[i] = treeNode;
        }
        Arrays.sort(nodeArr, new Comparator<TreeNode>() {
            @Override
            public int compare(TreeNode o1, TreeNode o2) {
                if (o2.height > o1.height) {
                    return 1;
                } else if (o2.height < o1.height) {
                    return -1;
                } else {
                    if (o1.spot < o2.spot) {
                        return 1;
                    }
                    return -1;
                }
            }
        });
        ArrayList<Integer> answer1 = new ArrayList<>();
        ArrayList<Integer> answer2 = new ArrayList<>();
        answer1.add(nodeArr[0].nodeNum);
        answer2.add(nodeArr[0].nodeNum);
        recursion(nodeArr, 0, nodeArr[0].spot, 0, 100000, 0, answer1);
        recursion(nodeArr, 0, nodeArr[0].spot, 0, 100000, 1, answer2);
        int[][] answer = new int[2][answer1.size()];
        for (int i = 0; i < answer1.size(); i++) {
            answer[0][i] = answer1.get(i);
            answer[1][i] = answer2.get(answer2.size() - 1 - i);
        }
        return answer;
    }

    public void recursion(TreeNode[] nodeArr, int nodeIndex, int nodeSpot, int leftLimit, int rightLimit, int direction, ArrayList<Integer> answer) {
        if (direction == 0) {
            leftSearch(nodeArr, nodeIndex, nodeSpot, leftLimit, direction, answer);
            rightSearch(nodeArr, nodeIndex, nodeSpot, rightLimit, direction, answer);
        } else {
            rightSearch(nodeArr, nodeIndex, nodeSpot, rightLimit, direction, answer);
            leftSearch(nodeArr, nodeIndex, nodeSpot, leftLimit, direction, answer);
        }
    }

    public void leftSearch(TreeNode[] nodeArr, int nodeIndex, int nodeSpot, int leftLimit, int direction, ArrayList<Integer> answer) {
        for (int i = nodeIndex + 1; i < nodeArr.length; i++) {
            if (nodeArr[i].spot < nodeSpot && nodeArr[i].spot >= leftLimit) {
                answer.add(nodeArr[i].nodeNum);
                recursion(nodeArr, i, nodeArr[i].spot, leftLimit, nodeSpot - 1, direction, answer);
                break;
            }
        }
    }

    public void rightSearch(TreeNode[] nodeArr, int nodeIndex, int nodeSpot, int rightLimit, int direction, ArrayList<Integer> answer) {
        for (int i = nodeIndex + 1; i < nodeArr.length; i++) {
            if (nodeArr[i].spot > nodeSpot && nodeArr[i].spot <= rightLimit) {
                answer.add(nodeArr[i].nodeNum);
                recursion(nodeArr, i, nodeArr[i].spot, nodeSpot + 1, rightLimit, direction, answer);
                break;
            }
        }
    }
}

class TreeNode {
    int nodeNum;
    int spot;
    int height;

    public TreeNode(int nodeNum, int spot, int height) {
        this.nodeNum = nodeNum;
        this.spot = spot;
        this.height = height;
    }
}
```



---

#### My logic & Feedback

이진트리(BST)를 응용하는 문제. 

문제의 핵심은 이진트리 자체를 '구현'하는 것이며, 

이진트리를 쉽게 구현하기 위해 Comparator 객체를 통해 TreeNode 2차원 배열을 정렬했다.

정렬 기준은 1. 노드의 x좌표(깊이), 2.노드의 y좌표 이며, 따라서 nodeArr 배열은 Top-down, Left to right 로 정렬된다.

정렬만 다 되면 TreeNode 객체를 for문으로 탐색하며 조건에 맞는 left child와 right child를 찾아 list에 넣으면 된다.

