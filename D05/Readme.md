<h1>Spiral Matrix</h1>
<p><br>
Given a matrix of size N x M. You have to find the Kth element which will obtain while traversing the matrix spirally starting from the top-left corner of the matrix.<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: N = 3, M = 3, K = 4, A[] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}<br>
&emsp;&emsp;Output: 6<br>
&emsp;&emsp;Explanation: Spiral traversal of matrix: {1, 2, 3, 6, 9, 8, 7, 4, 5}. Fourth element is 6.<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: N = 2, M = 2, K = 2 , A[] = {{1, 2},{3, 4}}<br> 
&emsp;&emsp;Output: 2<br>
&emsp;&emsp;Explanation: Spiral traversal of matrix: {1, 2, 4, 3}. Second element is 2.<br>
<br>
Your Task:<br>  
You don't need to read input or print anything. Complete the function findK() which takes the matrix A[ ][ ], number of rows N, number of columns M, and integer K as input parameters and returns the Kth element in the spiral traversal of the matrix.<br>
<br>
Expected Time Complexity: O(N*M)<br>
Expected Auxiliary Space: O(1)<br>
<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ K ≤ N*M ≤ 10^6<br>
<br></p>
