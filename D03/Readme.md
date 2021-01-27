<h1>Smallest Positive Integer that can not be represented as Sum</h1>
<p><br>
Given an array of size N, find the smallest positive integer value that cannot be represented as sum of some elements from the array.<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: N = 6 ,array[] = {1, 10, 3, 11, 6, 15}<br>
&emsp;&emsp;Output: 2<br>
&emsp;&emsp;Explanation: 2 is the smallest integer value that cannot be represented as sum of elements from the array.<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: N = 3, array[] = {1, 1, 1}<br>
&emsp;&emsp;Output: 4<br>
&emsp;&emsp;Explanation:<br> 
&emsp;&emsp;&emsp;&emsp;1 is present in the array.<br>  
&emsp;&emsp;&emsp;&emsp;2 can be created by combining two 1s.<br>
&emsp;&emsp;&emsp;&emsp;3 can be created by combining three 1s.<br>
&emsp;&emsp;&emsp;&emsp;4 is the smallest integer value that cannot be represented as sum of elements from the array.<br>
<br>
Your Task:<br>  
You dont need to read input or print anything. Complete the function smallestpositive() which takes the array and N as input parameters and returns the smallest positive integer value that cannot be represented as sum of some elements from the array.<br>
<br>
Expected Time Complexity: O(N * Log(N))<br>
Expected Auxiliary Space: O(1)<br>
<br>
<br>
<br>
Constraints:<br>
&emsp;&emsp; 1) 1 ≤ N ≤ 10^6<br>
&emsp;&emsp; 2) 1 ≤ array[i] ≤ 10^9<br>
&emsp;&emsp; 3) Array may contain duplicates.<br>
<br></p>
