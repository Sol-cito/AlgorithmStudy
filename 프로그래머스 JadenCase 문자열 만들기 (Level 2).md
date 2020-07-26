## 프로그래머스 JadenCase 문자열 만들기 (Level 2)

- adenCase 문자열 만들기

- darklight

  sublimevimemacs

  Java 

###### 문제 설명

JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

##### 제한 조건

- s는 길이 1 이상인 문자열입니다.
- s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
- 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )

##### 입출력 예

| s                     |        return         |
| --------------------- | :-------------------: |
| 3people unFollowed me | 3people Unfollowed Me |
| for the last week     |   For The Last Week   |



출처 : https://programmers.co.kr/learn/courses/30/lessons/12951



---



#### My solution (Java)

```java
class Solution {
  public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        sb.append(("" + s.charAt(0)).toUpperCase());
        int pointer = 1;
        while (pointer < s.length()) {
            char target = s.charAt(pointer);
            if (s.charAt(pointer - 1) == ' ') {
                sb.append(("" + s.charAt(pointer)).toUpperCase());
            } else {
                sb.append(("" + s.charAt(pointer)).toLowerCase());
            }
            pointer++;
        }
        return sb.toString();
    }
}
```



---

#### My logic & Feedback

아주 쉬운 문자열 자르기 문제.

단, 문자 사이에 띄어쓰기가 하나 이상 있을 수 있따는 점에 주의해야 한다.

(그걸 모르고 처음에 split으로 풀었다가 실패가 우르르 나와서 다시 풀었다)

pointer로 while문을 돌면서, '띄어쓰기 바로 다음 문자(단어 덩어리의 가장 첫 글자)'를 toUpperCase로 대문자로 바꾸고,

나머지는 모두 toLowerCase로 소문자로 바꾼 후 StringBuilder에 붙이면 된다.