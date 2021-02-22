<h1>Water the plants</h1>
<p><br>
A gallery with plants is divided into n parts, numbered : 0,1,2,3...n-1. There are provisions for attaching water sprinklers at every partition. A sprinkler with range x at partition i can water all partitions from i-x to i+x.
Given an array gallery[ ] consisting of n integers, where gallery[i] is the range of sprinkler at partition i (power==-1 indicates no sprinkler attached), return the minimum number of sprinklers that need to be turned on to water the complete gallery.<br>
If there is no possible way to water the full length using the given sprinklers, print -1.<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: n = 6, gallery[ ] = {-1, 2, 2, -1, 0, 0}<br>
&emsp;&emsp;Output: 2<br>
&emsp;&emsp;Explanation: Sprinklers at index 2 and 5 can water thefull gallery, span of sprinkler at index 2 = [0,4] and span of sprinkler at index 5 = [5,5].<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: n = 9, gallery[ ] = {2, 3, 4, -1, 2, 0, 0, -1, 0}<br>
&emsp;&emsp;Output: -1<br>
&emsp;&emsp;Explanation: No sprinkler can throw water at index 7. Hence all plants cannot be watered.<br>
<br>
Example 3:<br>
&emsp;&emsp;Input: n = 9, gallery[ ] = {2, 3, 4, -1, 0, 0, 0, 0, 0}<br>
&emsp;&emsp;Output: 3<br>
&emsp;&emsp;Explanation: Sprinkler at indexes 2, 7 and 8 together can water all plants.<br>
<br>
<br>
Your task:<br>
Your task is to complete the function min_sprinklers() which takes the array gallery[ ] and the integer n as input parameters and returns the value to be printed.<br>
<br>
Expected Time Complexity: O(NlogN)<br>
Expected Auxiliary Space: O(N)<br>
<br>
<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ n ≤ 10^5<br>
&emsp;&emsp;gallery[i] ≤ 50<br>
<br></p>
