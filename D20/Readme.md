<h1>Valentine Sum</h1>
<p><br>
Cupid wants to strike maximum houses in Geek Land on Valentine's Day. The houses in Geek Land are arranged in the form of a binary tree. Cupid is standing at target node initially. 
Find the sum of all nodes within a maximum distance k from target node. The target node should be included in the sum.<br>
<br>
Example 1:<br>
&emsp;&emsp;Input:<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;1<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;2&emsp;&emsp;&emsp;9<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;&emsp;/&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;4&emsp;&emsp;&emsp;5&emsp;&emsp;&emsp;7<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;\&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;8&emsp;&emsp;&emsp;19&emsp;&emsp;20&emsp;&emsp;&emsp;11<br>
&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;&emsp;/&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;30&emsp;&emsp;40&emsp;&emsp;&emsp;50<br>
<br>
&emsp;&emsp;target = 9, K = 1<br>
&emsp;&emsp;Output: 22<br>
&emsp;&emsp;Explanation:Nodes within distance 1 from 9 are 9, 5, 7, 1<br>  
<br>
Example 2:<br>
&emsp;&emsp;Input:<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;1<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;2&emsp;&emsp;&emsp;9<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;&emsp;/&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;4&emsp;&emsp;&emsp;5&emsp;&emsp;&emsp;7<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;\&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;8&emsp;&emsp;&emsp;19&emsp;&emsp;20&emsp;&emsp;&emsp;11<br>
&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;&emsp;/&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;30&emsp;&emsp;40&emsp;&emsp;&emsp;50<br>
<br>&emsp;&emsp;target = 40, K = 2<br>
&emsp;&emsp;Output: 113<br>
&emsp;&emsp;Explanation: Nodes within distance 2 from 40 are 40, 19, 50, 4<br>
<br>
Your Task:<br>
You don't need to read input or print anything. Complete the function sum_at_distK() which takes the root of the tree, target, and K  as input parameter and returns the sum of all nodes within a max distance of k from the target<br>
<br>
Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(N)<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ N, Node Value ≤ 10^5<br>
&emsp;&emsp;1 ≤ K ≤ 20<br>
<br></p>
