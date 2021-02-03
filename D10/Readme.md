<h1>Repeated String Match</h1>
<p><br>
Given two strings A and B, find the minimum number of times A has to be repeated such that B becomes a substring of the repeated A. If B cannot be a substring of A no matter how many times it is repeated, return -1.<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: A = "abcd", B = "cdabcdab"<br>
&emsp;&emsp;Output: 3<br>
&emsp;&emsp;Explanation: After repeating A three times, we get "abcdabcdabcd".<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: A = "aa", B = "a"<br>
&emsp;&emsp;Output: 1<br>
&emsp;&emsp;Explanation: B is already a substring of A.<br>
<br>
Your Task:  <br>
You don't need to read input or print anything. Complete the function repeatedStringMatch() which takes strings A and B as input parameters and returns the minimum number of operations to complete the task. If it is not possible then return -1.<br>
<br>
Expected Time Complexity: O(|A| * |B|)<br>
Expected Auxiliary Space: O(1)<br>
<br>
<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ |A|, |B| ≤ 10^3<br>
<br></p>
