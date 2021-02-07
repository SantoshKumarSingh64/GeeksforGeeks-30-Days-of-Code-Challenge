<h1>Bit Difference</h1>
<p><br>
Given an integer array of size  N . You have to find sum of bit differences in all pairs that can be formed from array elements. Bit difference of a pair (x, y) is count of different bits at same positions in binary representations of x and y.<br>
For example, bit difference for 2 and 7 is 2. Binary representation of 2 is 010 and 7 is 111 ( first and last bits differ in two numbers).<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: N = 2, arr[] = {1, 2}<br>
&emsp;&emsp;Output: 4<br>
&emsp;&emsp;Explanation: All possible pairs are [(1,1) (1,2) (2,1) (2,2)] their respective Bit differences are 0 ,  2 , 2 , 0<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: N = 5, arr[] = {3, 5, 2, 5, 2}<br>
&emsp;&emsp;Output: 36<br>
<br>
Your Task:<br>  
You don't need to read input or print anything. Complete the function sumBitDiff() which takes the array a[] and size of array N as input parameters and returns the answer<br>
<br>
Expected Time Complexity: O(NlogN)<br>
Expected Auxiliary Space: O(1)<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ N ≤ 10^5<br>
&emsp;&emsp;1 ≤ arr[i] ≤ 10^8<br>
<br></p>
