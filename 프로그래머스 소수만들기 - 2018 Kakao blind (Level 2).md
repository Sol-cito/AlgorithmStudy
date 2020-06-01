## 프로그래머스 소수만들기 - 2018 Summer/Winter Coding

- ###### 문제 설명

  주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

  ##### 제한사항

  - nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
  - nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

  ------

  ##### 입출력 예

  | nums        | result |
  | ----------- | ------ |
  | [1,2,3,4]   | 1      |
  | [1,2,7,6,4] | 4      |

  ##### 입출력 예 설명

  입출력 예 #1
  [1,2,4]를 이용해서 7을 만들 수 있습니다.

  입출력 예 #2
  [1,2,4]를 이용해서 7을 만들 수 있습니다.
  [1,4,6]을 이용해서 11을 만들 수 있습니다.
  [2,4,7]을 이용해서 13을 만들 수 있습니다.
  [4,6,7]을 이용해서 17을 만들 수 있습니다.

출처 : https://programmers.co.kr/learn/courses/30/lessons/12977



---

#### My first solution (Java) 

```java
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int[] selected = new int[3];
        for (int i = 0; i < nums.length - 2; i++) {
            selected[0] = nums[i];
            for (int j = i + 1; j < nums.length - 1; j++) {
                selected[1] = nums[j];
                for (int k = j + 1; k < nums.length; k++) {
                    selected[2] = nums[k];

                    int sum = selected[0] + selected[1] + selected[2];
                    int count = 0;
                    for (int x = 2; x < sum; x++) {
                        if (sum % x == 0) {
                            count++;
                        }
                    }
                    if (count == 0) {
                        answer++;
                    }
                }
            }
        }
        return answer;
    }
}
```

---

#### My logic & feedback

for문을 3개 써서 3개의 조합 수를 구한 후,

그 합을 다시한번 for문으로 나누어서 소수인지 판별하면 되는 쉬운 문제.