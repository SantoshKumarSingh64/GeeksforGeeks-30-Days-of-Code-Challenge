<h1>Count Triplets</h1>
<p><br>
Given a sorted linked list of distinct nodes (no two nodes have the same data) and an integer X. Count distinct triplets in the list that sum up to given integer X.<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: LinkedList: 1->2->4->5->6->8->9, X = 17<br>
&emsp;&emsp;Output: 2<br>
&emsp;&emsp;Explanation: Distinct triplets are (2, 6, 9) and (4, 5, 8) which have sum equal to X i.e 17.<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: LinkedList: 1->2->4->5->6->8->9, X = 15<br>
&emsp;&emsp;Output: 5<br>
&emsp;&emsp;Explanation: (1, 5, 9), (1, 6, 8), (2, 4, 9), (2, 5, 8), (4, 5, 6) are the distinct triplets.<br>
<br>
Your Task:<br>  
You don't need to read input or print anything. Complete the function countTriplets() which takes a head reference and X as input parameters and returns the triplet count.<br>
<br>
Expected Time Complexity: O(N^2)<br>
Expected Auxiliary Space: O(N)<br>
<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ Number of Nodes ≤ 10^3<br> 
&emsp;&emsp;1 ≤ Node value ≤ 10^4<br>
<br></p>
