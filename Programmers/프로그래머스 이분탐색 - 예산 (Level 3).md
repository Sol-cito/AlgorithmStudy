## 프로그래머스 이분탐색 - 예산 (Level 3)

**문제 설명**

국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것입니다. 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있습니다. 그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정합니다.

1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정합니다.
2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정합니다. 
   상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정합니다. 
예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150일 때, 상한액을 127로 잡으면 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 됩니다.
각 지방에서 요청하는 예산이 담긴 배열 budgets과 총 예산 M이 매개변수로 주어질 때, 위의 조건을 모두 만족하는 상한액을 return 하도록 solution 함수를 작성해주세요.

**제한 사항**
지방의 수는 3 이상 100,000 이하인 자연수입니다.
각 지방에서 요청하는 예산은 1 이상 100,000 이하인 자연수입니다.
총 예산은 지방의 수 이상 1,000,000,000 이하인 자연수입니다.

**입출력 예**
budgets	M	return
[120, 110, 140, 150]

출처 : https://programmers.co.kr/learn/courses/30/lessons/43237



---



#### My solution (Java)

```java
import java.util.Arrays;

class Solution {  
    public int solution(int[] budgets, int M) {
		int answer = 0;
		int left = 1;
		int right = M;
		int mid = (left + right) / 2;
		int preMid = 0;
		int length = budgets.length;
		Arrays.sort(budgets);

		while (true) {
			if (mid == preMid) {
				break;
			}
			int totalBudget = M;
			boolean lackOfBudget = false;
			for (int i = 0; i < length; i++) {
				if (totalBudget < 0) { // 예산이 모자라는 경우
					lackOfBudget = true;
					break;
				}
				if (budgets[i] >= mid) { // 예산이 상한액보다 크거나 같으면 상한액만큼 준다.
					totalBudget -= mid;
				} else { // 예산이 상한액보다 적으면 예산만큼 다 준다.
					totalBudget -= budgets[i];
				}
			}
			if (lackOfBudget || totalBudget < 0) {
				right = mid;
				preMid = mid;
				mid = (left + right) / 2;
			} else {
				left = mid;
				preMid = mid;
				mid = (left + right) / 2;
			}
		}
		if (mid > budgets[length - 1]) {
			answer = budgets[length - 1]; //모든 지방의 예산을 충족시킨다면, 요청 금액을 그대로 배정한다.
		} else {
			answer = mid; //그게 아니라면, 가장 최적의 예산을 배정한다.
		}
		return answer;
	}
}
```



---



#### My logic

전형적인 이중탐색 문제다.

상한액의 최소값 - 최대값 사이를 이분탐색으로 왔다갔다하면서 조건을 만족시키는 부분(mid == preMid) 에서 멈춘 뒤, mid값이 모든 지방의 예산을 충족시킨다면 budgets중 가장 큰 값을 반환(위에서 정렬했으므로 가장 마지막 index), 그게 아니라면 mid값을 반환하면 된다.

