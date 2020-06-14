## 프로그래머스 방금그곡 - 2018 Kakao blind (Level 2)

###### 문제 설명

라디오를 자주 듣는 네오는 라디오에서 방금 나왔던 음악이 무슨 음악인지 궁금해질 때가 많다. 그럴 때 네오는 다음 포털의 '방금그곡' 서비스를 이용하곤 한다. 방금그곡에서는 TV, 라디오 등에서 나온 음악에 관해 제목 등의 정보를 제공하는 서비스이다.

네오는 자신이 기억한 멜로디를 가지고 방금그곡을 이용해 음악을 찾는다. 그런데 라디오 방송에서는 한 음악을 반복해서 재생할 때도 있어서 네오가 기억하고 있는 멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수도 있다. 반대로, 한 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다. 그렇기 때문에 네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다. 다음과 같은 가정을 할 때 네오가 찾으려는 음악의 제목을 구하여라.

- 방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.
- 네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
- 각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
- 음악이 00:00를 넘겨서까지 재생되는 일은 없다.
- 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
- 조건이 일치하는 음악이 없을 때에는 `(None)`을 반환한다.

### 입력 형식

입력으로 네오가 기억한 멜로디를 담은 문자열 `m`과 방송된 곡의 정보를 담고 있는 배열 `musicinfos`가 주어진다.

- m`은 음 `1`개 이상 `1439`개 이하로 구성되어 있다.

- musicinfos는 100개 이하의 곡 정보를 담고 있는 배열로, 각각의 곡 정보는 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열이다.

- 음악의 시작 시각과 끝난 시각은 24시간 `HH:MM` 형식이다.
- 음악 제목은 '`,`' 이외의 출력 가능한 문자로 표현된 길이 `1` 이상 `64` 이하의 문자열이다.
- 악보 정보는 음 `1`개 이상 `1439`개 이하로 구성되어 있다.

### 출력 형식

조건과 일치하는 음악 제목을 출력한다.

### 입출력 예시

| m                | musicinfos                                             | answer |
| ---------------- | ------------------------------------------------------ | ------ |
| ABCDEFG          | [12:00,12:14,HELLO,CDEFGAB, 13:00,13:05,WORLD,ABCDEF]  | HELLO  |
| CC#BCC#BCC#BCC#B | [03:00,03:30,FOO,CC#B, 04:00,04:08,BAR,CC#BCC#BCC#B]   | FOO    |
| ABC              | [12:00,12:14,HELLO,C#DEFGAB, 13:00,13:05,WORLD,ABCDEF] | WORLD  |

### 설명

첫 번째 예시에서 HELLO는 길이가 7분이지만 12:00부터 12:14까지 재생되었으므로 실제로 CDEFGABCDEFGAB로 재생되었고, 이 중에 기억한 멜로디인 ABCDEFG가 들어있다.
세 번째 예시에서 HELLO는 C#DEFGABC#DEFGAB로, WORLD는 ABCDE로 재생되었다. HELLO 안에 있는 ABC#은 기억한 멜로디인 ABC와 일치하지 않고, WORLD 안에 있는 ABC가 기억한 멜로디와 일치한다.

출처 : https://programmers.co.kr/learn/courses/30/lessons/17683



---

#### My first solution (Java) 

```java
import java.util.ArrayList;
import java.util.Collections;

class Solution {
      public String solution(String m, String[] musicinfos) {
        String answer = "";

        /* m 자르기 */
        char[] splited = m.toCharArray();
        ArrayList<String> mList = new ArrayList<>();
        for (int i = 0; i < splited.length; i++) {
            if (i < splited.length - 1 && splited[i + 1] == '#') {
                mList.add("" + splited[i] + splited[i + 1]);
                i++;
            } else {
                mList.add("" + splited[i]);
            }
        }
        /* 클래스 만들기 */
        ArrayList<Musicinfo> list = new ArrayList<>();
        for (String each : musicinfos) {
            Musicinfo musicinfo = new Musicinfo(each);
            list.add(musicinfo);
        }
        ArrayList<Musicinfo> resultList = new ArrayList<>();
        for (int i = 0; i < list.size(); i++) {
            Musicinfo musicinfo = list.get(i);
            if (musicinfo.duration >= mList.size()) {
                ArrayList<String> letterList = musicinfo.letterList;
                for (int j = 0; j < letterList.size() - mList.size() + 1; j++) {
                    int mListPointer = 0;
                    int letterListPointer = j;
                    boolean check = true;
                    while (mListPointer < mList.size() && check) {
                        if (!mList.get(mListPointer).equals(letterList.get(letterListPointer))) {
                            check = false;
                        }
                        mListPointer++;
                        letterListPointer++;
                    }
                    if (check) {
                        resultList.add(musicinfo);
                        break;
                    }
                }
            }
        }
        if (resultList.size() == 0) {
            answer = "(None)";
            return answer;
        }
        Collections.sort(resultList);
        answer = resultList.get(0).musicName;
        return answer;
    }
}

class Musicinfo implements Comparable<Musicinfo> {
    int duration;
    String musicName;
    ArrayList<String> letterList;

    public Musicinfo(String musicInfo) {
        String[] splited = musicInfo.split(",");
        int hour = 60 * (Integer.parseInt("" + splited[1].charAt(0) + splited[1].charAt(1))
                - Integer.parseInt("" + splited[0].charAt(0) + splited[0].charAt(1)));
        int minute = Integer.parseInt("" + splited[1].charAt(3) + splited[1].charAt(4))
                - Integer.parseInt("" + splited[0].charAt(3) + splited[0].charAt(4));
        this.duration = hour + minute;
        this.musicName = splited[2];
        
        letterList = new ArrayList<>();
        char[] splitedNote = splited[3].toCharArray();
        int count = 0;
        int pointer = 0;
        while (duration > count) {
            if (pointer < splitedNote.length - 1 && splitedNote[pointer + 1] == '#') {
                letterList.add("" + splitedNote[pointer] + splitedNote[pointer + 1]);
                pointer++;
            } else {
                letterList.add("" + splitedNote[pointer]);
            }
            pointer++;
            count++;
            if (pointer >= splitedNote.length) {
                pointer = 0;
            }
        }
    }

    @Override
    public int compareTo(Musicinfo o) {
        if (this.duration > o.duration) {
            return -1;
        } else if (this.duration < o.duration) {
            return 1;
        }
        return 0;
    }
}
```

---

#### My logic & feedback

문자열 처리 + 객체 정렬 + 탐색이 결합되어있는 문제다.

문자열 처리는 musicinfo 객체를 생성하는 부분에서 처리하였고(split 이용)

정렬은 compareTo 메소드 구현을 통해 해결하였다.

m이 어떤 음악을 가리키는지 탐색하는 것은 이중 포문으로 해결.