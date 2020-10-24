## Leetcode - Coin Change [Medium]

ou are given coins of different denominations and a total amount of money *amount*. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

 

**Example 1:**

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**

```
Input: coins = [2], amount = 3
Output: -1
```

**Example 3:**

```
Input: coins = [1], amount = 0
Output: 0
```

**Example 4:**

```
Input: coins = [1], amount = 1
Output: 1
```

**Example 5:**

```
Input: coins = [1], amount = 2
Output: 2
```

 

**Constraints:**

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 231 - 1`
- `0 <= amount <= 104`

Link : https://leetcode.com/problems/coin-change/



---



#### My solution (Java)

```java
class Solution {
  public int coinChange(int[] coins, int amount) {
        if (amount == 0) return 0;
        Arrays.sort(coins);
        Queue<Coin> que = new LinkedList<>();
        Set<Integer> set = new HashSet<>();
        for (int i = coins.length - 1; i >= 0; i--) {
            que.add(new Coin(coins[i], 1, i));
            set.add(coins[i]);
        }
        while (!que.isEmpty()) {
            Coin polled = que.poll();
            if (polled.amount == amount) {
                return polled.cnt;
            }
            for (int i = polled.index; i >= 0; i--) {
                if (!set.contains(polled.amount + coins[i]) && polled.amount <= amount) {
                    set.add(polled.amount + coins[i]);
                    que.add(new Coin(polled.amount + coins[i], polled.cnt + 1, i));
                }
            }
        }
        return -1;
    }
}

class Coin {
    int amount;
    int cnt;
    int index;

    public Coin(int amount, int cnt, int index) {
        this.amount = amount;
        this.cnt = cnt;
        this.index = index;
    }
}

```

---



#### My logic & Feedback

딱 봐도 DP문제인데, 풀이 방법이 생각나지 않아 일단 BFS로 풀었다...

속도와 메모리가 당연히 효율적으로 나오지 않아서 불만족스럽다.

이 문제를 다시 풀면서 DP 개념과 풀이방법을 한번 더 재정비해야될 것 같다.