## 프로그래머스 다음 큰 숫자 (Level 2)

- ###### 문제 설명

  자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

  - 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
  - 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
  - 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

  예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

  자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

  ##### 제한 사항

  - n은 1,000,000 이하의 자연수 입니다.

  ------

  ##### 입출력 예

  | n    | result |
  | ---- | ------ |
  | 78   | 83     |
  | 15   | 23     |

  ##### 입출력 예 설명

  입출력 예#1
  문제 예시와 같습니다.
  입출력 예#2
  15(1111)의 다음 큰 숫자는 23(10111)입니다.

| n    | result |
| ---- | ------ |
| 78   | 83     |
| 15   | 23     |

출처 : https://programmers.co.kr/learn/courses/30/lessons/12911



---



#### My solution (Java)

```java
class Solution {
 public int solution(int n) {
        int answer = 0;
        int numOfOne = countOne(n);
        for (int i = n + 1; ; i++) {
            if (countOne(i) == numOfOne) {
                return i;
            }
        }
    }

    public int countOne(int n) {
        int count = 1;
        while (n > 1) {
            if (n % 2 == 1) {
                count++;
            }
            n = n - n / 2 - n % 2;
        }
        return count;
    }
}
```



---

#### My logic & Feedback

2진법으로 변환하는것이 포인트. 진법 변환의 원리를 알면 쉽다.

나머지와 몫으로 진법변환하는 method를 만들고, 그 중 1의 개수가 일치하면서 가장 작은 수를 return하면 끝이다.