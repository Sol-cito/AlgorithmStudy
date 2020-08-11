## 프로그래머스 n진수 게임 - 2018 Kakao blind (Level 2)

###### 문제 설명

튜브가 활동하는 코딩 동아리에서는 전통적으로 해오는 게임이 있다. 이 게임은 여러 사람이 둥글게 앉아서 숫자를 하나씩 차례대로 말하는 게임인데, 규칙은 다음과 같다.

1. 숫자를 0부터 시작해서 차례대로 말한다. 첫 번째 사람은 0, 두 번째 사람은 1, … 열 번째 사람은 9를 말한다.
2. 10 이상의 숫자부터는 한 자리씩 끊어서 말한다. 즉 열한 번째 사람은 10의 첫 자리인 1, 열두 번째 사람은 둘째 자리인 0을 말한다.

이렇게 게임을 진행할 경우,
`0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3, 1, 4, …`
순으로 숫자를 말하면 된다.

한편 코딩 동아리 일원들은 컴퓨터를 다루는 사람답게 이진수로 이 게임을 진행하기도 하는데, 이 경우에는
`0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, …`
순으로 숫자를 말하면 된다.

이진수로 진행하는 게임에 익숙해져 질려가던 사람들은 좀 더 난이도를 높이기 위해 이진법에서 십육진법까지 모든 진법으로 게임을 진행해보기로 했다. 숫자 게임이 익숙하지 않은 튜브는 게임에 져서 벌칙을 받는 굴욕을 피하기 위해, 자신이 말해야 하는 숫자를 스마트폰에 미리 출력해주는 프로그램을 만들려고 한다. 튜브의 프로그램을 구현하라.

### 입력 형식

진법 `n`, 미리 구할 숫자의 갯수 `t`, 게임에 참가하는 인원 `m`, 튜브의 순서 `p` 가 주어진다.

- 2 ≦ `n` ≦ 16
- 0 ＜ `t` ≦ 1000
- 2 ≦ `m` ≦ 100
- 1 ≦ `p` ≦ `m`

### 출력 형식

튜브가 말해야 하는 숫자 `t`개를 공백 없이 차례대로 나타낸 문자열. 단, `10`~`15`는 각각 대문자 `A`~`F`로 출력한다.

### 입출력 예제

| n    | t    | m    | p    | result           |
| ---- | ---- | ---- | ---- | ---------------- |
| 2    | 4    | 2    | 1    | 0111             |
| 16   | 16   | 2    | 1    | 02468ACE11111111 |
| 16   | 16   | 2    | 2    | 13579BDF01234567 |

출처 : https://programmers.co.kr/learn/courses/30/lessons/17687



---

#### My first solution (Java) 

```java
import java.util.Stack;

class Solution {
         public String solution(int n, int t, int m, int p) {
        StringBuilder answer = new StringBuilder();
        int limit = t * m;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; sb.length() < limit; i++) {
            Stack<Integer> stack = new Stack<>();
            int targetNum = i;
            while (true) {
                int quotient = targetNum / n;
                int remainder = targetNum % n;
                stack.add(remainder);
                if (quotient < n) {
                    if (quotient < n && quotient != 0) {
                        stack.add(quotient);
                    }
                    break;
                }
                targetNum = quotient;
            }
            String popedLetter = "";
            while (!stack.isEmpty()) {
                int poped = stack.pop();
                if (poped >= 10) {
                    String above = "ABCDEF";
                    popedLetter += above.charAt(poped % 10);
                } else {
                    popedLetter += poped;
                }
            }
            if (sb.length() <= limit) {
                sb.append(popedLetter);
            }
        }
        int pointer = 0;
        while (answer.length() < t) {
            answer.append(sb.toString().charAt(pointer + p - 1));
            pointer += m;
        }
        return answer.toString();
    }
}
```

---

#### My logic & feedback

n진수를 몫과 나머지, 그리고 stack을 이용해 구현했다.

어떤 수 x를 n진수로 표현하는 방법으로, 몫이 n 미만이 될 때 까지 재귀적으로 나누기를 하고, 나머지를 붙여주는 방법을 생각해봤다.

예를들어 14를 3진수로 표현하는 방법은,

14/3 => 몫 4, 나머지 2 : 몫이 3보다 크므로 몫을 다시 3으로 나눈다.

4/3 => 몫 1, 나머지 1 : 몫이 3보다 작으므로 멈춤.

이므로 112 로 표현할 수 있다.

위 계산의 결과는 가장 마지막에 계산한 결과부터 입력되어야 하므로 후입선출의 자료구조인 stack을 써서 표현 가능하다.

