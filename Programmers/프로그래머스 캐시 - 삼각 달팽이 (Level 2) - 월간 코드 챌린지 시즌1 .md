## 프로그래머스 캐시 - 삼각 달팽이 (Level 2) - 월간 코드 챌린지 시즌1 

**문제설명**

정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

![examples.png](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/e1e53b93-dcdf-446f-b47f-e8ec1292a5e0/examples.png)

------

##### 제한사항

- n은 1 이상 1,000 이하입니다.

------

##### 입출력 예

| n    | result                                                    |
| ---- | --------------------------------------------------------- |
| 4    | `[1,2,9,3,10,8,4,5,6,7]`                                  |
| 5    | `[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]`                   |
| 6    | `[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]` |

------

##### 입출력 예 설명

입출력 예 #1

- 문제 예시와 같습니다.

입출력 예 #2

- 문제 예시와 같습니다.

입출력 예 #3

- 문제 예시와 같습니다.



출처 : https://programmers.co.kr/learn/courses/30/lessons/68645

---



#### My solution (Java)

```java
import java.util.ArrayList;

class Solution {
    int num = 1;

    public int[] solution(int n) {
        ArrayList<int[]> arrList = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            int[] arr = new int[i];
            arrList.add(arr);
        }

        int length = n;
        for (int i = 0; length > 0; i += 2) {
            makeSnail(arrList, i, i / 2, length);
            length -= 3;
        }
        int answerSize = 0;
        for (int i = 1; i <= n; i++) {
            answerSize += i;
        }
        int[] answer = new int[answerSize];
        int index = 0;
        for (int[] eachArr : arrList) {
            for (int each : eachArr) {
                answer[index] = each;
                index++;
            }
        }
        return answer;
    }

    public void makeSnail(ArrayList<int[]> arrList, int x, int y, int length) {
        /* 위에서 왼쪽 */
        int targetX = x;
        for (int i = 0; i < length; i++) {
            arrList.get(targetX)[y] = num;
            targetX++;
            num++;
        }
        /* 가장 아래 */
        int targetY = y + 1;
        for (int i = 1; i < length; i++) {
            arrList.get(arrList.size() - 1 - y)[targetY] = num;
            targetY++;
            num++;
        }
        /* 가장 오른쪽 */
        targetY = arrList.size() - 2 - y;
        for (int i = 2; i < length; i++) {
            arrList.get(targetY)[arrList.get(targetY).length - 1 - y] = num;
            targetY--;
            num++;
        }
    }
}
```

---



#### My logic & Feedback

빡구현이 요구되는 문제다. 꼼수 따윈 없는 것 같다...

빡구현 문제는 상당한 스트레스를 요한다. 특히 이런 배열의 index를 이용하는 구현문제는...

index가 하나만 어긋나도 error가 뜨거나 답이 틀린다..그래서 상당한 집중력과 구현력을 요한다..

풀었긴 하나 굉장히 스트레스 받았던 빡구현 문제..후..



