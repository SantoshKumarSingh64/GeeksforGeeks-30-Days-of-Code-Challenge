<h1>Project Manager</h1>
<p><br>
An IT company is working on a large project. The project is broken into N modules and distributed to different teams. The amount of time (in months) required to complete each module is given in an array duration[ ]. Two modules can be processed simultaneously only if their is no dependency between them and it is given that M modules have interdependecies. 
As the project manager, compute the minimum time required to complete the project.<br>
<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: N = 6 6<br>
&emsp;&emsp;duration[] = {1, 2, 3, 1, 3, 2}<br>
&emsp;&emsp;dependencies:<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;5 2<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;5 0<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;4 0<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;4 1<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;2 3<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;3 1<br>
&emsp;&emsp;Output: 8<br>
&emsp;&emsp;Explanation:<br>
<br>
&emsp;&emsp;&emsp;&emsp;<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/graph.png" height="200"><br>
<br>
&emsp;&emsp;&emsp;&emsp;The Graph of dependency forms this and the project will be completed when Module 1 is completed which takes 8 months.<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: N = 3 3<br>
&emsp;&emsp;duration[] = {5, 5, 5}<br>
&emsp;&emsp;dependencies:<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;0 1<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;1 2<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;2 0<br>
&emsp;&emsp;Output: -1<br>
&emsp;&emsp;Explanation: There is a cycle in the dependency graph hence the project cannot be completed.<br>
<br>
<br>
Your Task:<br>
Complete the function minTime() which takes N, M, duration array, and dependencies array as input parameter and return the minimum time required. Return -1 if the project can not be completed. <br>
<br>
Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(N)<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ N ≤ 10^5<br>
&emsp;&emsp;1 ≤ M ≤ 2*10^5<br>
&emsp;&emsp;1 ≤ duration[i] ≤ 10^5<br>
<br></p>
