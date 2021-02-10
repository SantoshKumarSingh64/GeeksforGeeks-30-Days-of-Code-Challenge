<h1>Restrictive Candy Crush</h1>
<p><br>
Given a string S and an integer K, the task is to reduce the string by applying the following operation:<br>
Choose a group of K consecutive identical characters and remove them. The operation can be performed any number of times until it is no longer possible.<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: K = 2, S = "geeksforgeeks"<br>
&emsp;&emsp;Output: gksforgks<br>
&emsp;&emsp;Explanation: Modified String after each step: "geegsforgeeks" -> "gksforgks"<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: K = 2, S = "geegsforgeeeks"<br> 
&emsp;&emsp;Output: sforgeks<br>
&emsp;&emsp;Explanation: Modified String after each step: "geegsforgeeeks" -> "ggsforgeks" -> "sforgeks"<br>
<br>
Your Task:<br>  
You don't need to read input or print anything. Complete the function Reduced_String() which takes integer K and string S as input parameters and returns the reduced string.<br>
<br>
Expected Time Complexity: O(|S|)<br>
Expected Auxiliary Space: O(|S|)<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ |S| ≤ 10^5<br>
&emsp;&emsp;1 ≤ K ≤ |S|<br>
<br></p>
