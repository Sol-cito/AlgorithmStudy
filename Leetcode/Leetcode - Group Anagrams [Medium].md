## Leetcode - Group Anagrams [Medium]

Given an array of strings, group anagrams together.

**Example:**

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

**Note:**

- All inputs will be in lowercase.
- The order of your output does not matter.

Link : https://leetcode.com/problems/group-anagrams/



---



#### My solution (Java)

```java
class Solution {
     public List<List<String>> groupAnagrams(String[] strs) {
        Set<String> set = new HashSet<>();
        HashMap<String, List<String>> map = new HashMap<>();
        for (String element : strs) {
            StringBuilder sb = new StringBuilder();
            char[] tempArr = element.toCharArray();
            Arrays.sort(tempArr);
            for (char eachChar : tempArr) {
                sb.append(eachChar);
            }
            String result = sb.toString();
            if (map.get(result) == null) {
                ArrayList<String> list = new ArrayList<>();
                list.add(element);
                map.put(result, list);
                set.add(result);
            } else {
                map.get(result).add(element);
            }
        }
        List<List<String>> result = new ArrayList<>();
        for(String element : set){
            result.add(map.get(element));
        }
        return result;
    }
}

```

---



#### My logic & Feedback

So the key to this question is to make group lists sorted by the same anagram. 

I firstly divide each input string into characters, alphabetically sort them, and put them together again by using string builder (way faster than manipulating string itself).

By doing so, I can figure out whether I have to make a new list for a new anagram or which existing anagram list each string should be added to.

And I also use hash map to store original string value of each element so that I can finally put them into the result list, as well as set to store keys for the map.