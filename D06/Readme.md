<h1>Coins of Geekland</h1>
<p><br>
In Geekland there is a grid of coins of size N x N. You have to find the maximum sum of coins in any sub-grid of size K x K.<br>
Note: Coins of the negative denomination are also possible at Geekland.<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: N = 5, K = 3<br> 
&emsp;&emsp;mat[[]] = {1, 1, 1, 1, 1}<br> 
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;{2, 2, 2, 2, 2} <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;{3, 8, 6, 7, 3} <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;{4, 4, 4, 4, 4} <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;{5, 5, 5, 5, 5}<br>
&emsp;&emsp;Output: 48<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;{8, 6, 7}<br>
&emsp;&emsp;Explanation:&emsp;{4, 4, 4}&emsp;&emsp;has the maximum sum 48.<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;{5, 5, 5} <br>
<br>
Example 2:<br>
&emsp;&emsp;Input: N = 1, K = 1<br>
&emsp;&emsp;mat[[]] = {{4}} <br>
&emsp;&emsp;Output: 4<br>
<br>
Your Task:<br>  
You don't need to read input or print anything. Complete the function Maximum_Sum() which takes the matrix mat[], size of Matrix N, and value K as input parameters and returns the maximum sum.<br>
<br>
Expected Time Complexity: O(N^2)<br>
Expected Auxiliary Space: O(N^2)<br>
<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ K ≤ N ≤ 10^3<br>
&emsp;&emsp;-5*105 ≤ mat[i][j] ≤ 5*10^5<br>
<br></p>
