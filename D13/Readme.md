<h1>Check Tree Traversal</h1>
<p><br>
Given Preorder, Inorder and Postorder traversals of some tree of size N. The task is to check if they are all of the same tree or not.<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: N = 5<br>
&emsp;&emsp;preorder[ ] = {1, 2, 4, 5, 3}<br>
&emsp;&emsp;inorder[ ] = {4, 2, 5, 1, 3}<br>
&emsp;&emsp;postorder[ ] = {4, 5, 2, 3, 1}<br>
&emsp;&emsp;Output: Yes<br>
&emsp;&emsp;Explanation: All of the above three traversals are of the same tree.<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;1<br>
&emsp;&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;2&emsp;&emsp;&emsp;3<br>
&emsp;&emsp;&emsp;/&emsp;&emsp;\<br>
&emsp;&emsp;4&emsp;&emsp;&emsp;5<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: N = 5<br>
&emsp;&emsp;preorder[ ] = {1, 5, 4, 2, 3}<br>
&emsp;&emsp;inorder[ ] = {4, 2, 5, 1, 3}<br>
&emsp;&emsp;postorder[ ] = {4, 1, 2, 3, 5}<br>
&emsp;&emsp;Output: No<br>
&emsp;&emsp;Explanation: The three traversals can not be of the same tree.<br>
<br>
Your Task:<br>
You don't need to read input or print anything. Complete the function checktree() which takes the array preorder[ ], inorder[ ], postorder[ ] and integer N as input parameters and returns true if the three traversals are of the same tree or not.<br>
<br>
Expected Time Complexity: O(N^2)<br>
Expected Auxiliary Space: O(N)<br>
<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ N ≤ 10^3<br>
<br></p>
