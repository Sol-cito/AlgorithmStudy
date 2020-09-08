## Leetcode - Evaluate Reverse Polish Notation [Medium]

Evaluate the value of an arithmetic expression in [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

Valid operators are `+`, `-`, `*`, `/`. Each operand may be an integer or another expression.

**Note:**

- Division between two integers should truncate toward zero.
- The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

**Example 1:**

```
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2:**

```
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

**Example 3:**

```
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

Link : https://leetcode.com/problems/evaluate-reverse-polish-notation/



---



#### My solution (Java)

```java
class Solution {
    public int evalRPN(String[] tokens) {
      if(tokens.length == 0){
            return 0;
        }
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < tokens.length; i++) {
            if (tokens[i].equals("+")) {
                stack.push(stack.pop() + stack.pop());
            } else if (tokens[i].equals("-")) {
                int firstPop = stack.pop();
                int secondPop = stack.pop();
                stack.push(secondPop - firstPop);
            } else if (tokens[i].equals("*")) {
                stack.push(stack.pop() * stack.pop());
            } else if (tokens[i].equals("/")) {
                int firstPop = stack.pop();
                int secondPop = stack.pop();
                stack.push(secondPop / firstPop);
            } else {
                stack.push(Integer.parseInt(tokens[i]));
            }
        }
        return stack.pop();
    }
}
```

---



#### My logic & Feedback

자료구조 수업에서 배운 내용이 문제로 나왔다.

Stack과 후위표기법에 관한 문제인데, Stack으로 각 element를 순서대로 push하고, 

연산기호가 나오면 스택의 2개를 pop해서 연산한 후 그 결과를 stack에 넣는 작업을 반복하면 된다.