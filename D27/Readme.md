<h1>Police and Thieves</h1>
<p><br>
Given an array of size n such that each element contains either a 'P' for policeman or a 'T' for thief. Find the maximum number of thieves that can be caught by the police. 
Keep in mind the following conditions :<br>
&emsp;&emsp;1. Each policeman can catch only one thief.<br>
&emsp;&emsp;2. A policeman cannot catch a thief who is more than K units away from him.<br>
<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: N = 5, K = 1, arr[] = {P, T, T, P, T}<br>
&emsp;&emsp;Output: 2<br>
&emsp;&emsp;Explanation: Maximum 2 thieves can be caught. First policeman catches first thief and second police man can catch either second or third &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;thief.<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: N = 6, K = 2, arr[] = {T, T, P, P, T, P}<br>
&emsp;&emsp;Output: 3<br>
&emsp;&emsp;Explanation: Maximum 3 thieves can be caught.<br>
<br>
<br>
Your Task:<br>
You dont need to read input or print anything. Complete the function catchThieves() that takes n, k and arr[ ] as input parameters and returns the maximum number of thieves that can be caught by the police. <br>
<br>
Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(N)<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ n ≤ 10^5<br>
&emsp;&emsp;1 ≤ k ≤ 100<br>
&emsp;&emsp;arr[i] = 'P' or 'T'<br>
<br></p>
