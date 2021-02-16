<h1>Shortest Range in BST</h1>
<p><br>
Given a BST (Binary Search Tree), find the shortest range [x, y], such that, at least one node of every level of the BST lies in the range.<br>
If there are multiple ranges with the same gap (i.e. (y-x)) return the range with the smallest x.<br>
<br>
Example 1:<br>
Input:<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;8<br>
&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;3&emsp;&emsp;&emsp;&emsp;&emsp;10<br>
&emsp;&emsp;/&emsp;&emsp;\&emsp;&emsp;&emsp;&emsp;&emsp;\<br>
&emsp;2&emsp;&emsp;&emsp;6&emsp;&emsp;&emsp;&emsp;&emsp;14<br>
&emsp;&emsp;&emsp;/&emsp;&emsp;&emsp;\&emsp;&emsp;&emsp;/<br>
&emsp;&emsp;&emsp;4&emsp;&emsp;&emsp;7&emsp;&emsp;12<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;11&emsp;&emsp;&emsp;13<br>
<br>
Output: 6 11<br>
Explanation: Level order traversal of the tree is [8], [3, 10], [2, 6, 14], [4, 7, 12], [11, 13]. The shortest range which satisfies the above mentioned condition is [6, 11]. <br>
<br>
Example 2:<br>
Input:<br>
<br>
&emsp;&emsp;&emsp;&emsp;12<br>
&emsp;&emsp;&emsp;&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;13<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;14<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;15<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;16<br>
<br>
&emsp;&emsp;Output: 12 16<br>
&emsp;&emsp;Explanation: Each level contains one node, so the shortest range is [12, 16].<br>
<br>
Your Task:<br>
You don't need to read input or print anything. Complete the function shortestRange() which takes the root of the tree as an input parameter and returns the pair of numbers<br>
<br>
Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(N)<br>
<br>
<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ N ≤ 10^5<br>
&emsp;&emsp;1 ≤ Node Value ≤ 10^4<br>
<br></p>
