<h1>Elixir of Life</h1>
<p><br>
Flamel is making the Elixir of Life but he is missing a secret ingredient, a set of contiguous plants (substring) from the Garden of Eden. The garden consists of various plants represented by string S where each letter represents a different plant.  But the prophecy has predicted that the correct set of plants required to make the potion will appear in the same contiguous pattern (substring) at the beginning of the forest (prefix), the end of the forest (suffix), and will also be the most frequent sequence present in the entire forest.<br>
<br>
Identify the substring of plants required to make the elixir and find out the number of times it appears in the forest. <br>
<br>
Example 1:<br>
&emsp;&emsp;Input: S = "ababaaaab"<br>
&emsp;&emsp;Output: 3<br>
&emsp;&emsp;Explanation: substring "ab" is a prefix, a suffix and appears 3 times.<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: S = "aaaa"<br>
&emsp;&emsp;Output: 4<br>
&emsp;&emsp;Explanation: substring "aaaa" occurs 1 time, substring "aaa" occurs 2 times, substring "aa" occurs 3 times, substring "a" occurs 4 times. All &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;of them are proper prefixes and suffixes. But, "a" has the maximum frequency.<br>
<br>
Example 3:<br>
&emsp;&emsp;Input: S = "abcdef"<br>
&emsp;&emsp;Output: 1<br>
<br>
<br>
Your Task:<br> 
You don't need to read input or print anything. Complete the function maxFrequency() which takes string S as input parameter and returns the answer<br>
<br>
Expected Time Complexity: O(NlogN)<br>
Expected Auxiliary Space: O(N)<br>
<br>
Constraints:<br> 
&emsp;&emsp;1 ≤ |S| ≤ 10^5<br>
<br></p>
