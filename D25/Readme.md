<h1>Spidy Sense</h1>
<p><br>
Spiderman is stuck in a difficult situation. His arch-enemy the Green Goblin has planted several of his infamous Pumpkin Bombs in various locations in a building. Help Spiderman activate his Spidey Sense and identify the impact zones. 
He has a blueprint of the building which is a M x N matrix that is filled with the characters ‘O’, ‘B’, and ‘W’ where:<br> 
&emsp;&emsp;‘O’ represents an open space.<br>
&emsp;&emsp;‘B’ represents a bomb.<br>
&emsp;&emsp;‘W’ represents a wall.<br>
<br>
You have to replace all of the O’s (open spaces) in the matrix with their shortest distance from a bomb without being able to go through any walls. Also, replace the bombs with 0 and walls with -1 in the resultant matrix. If no path exists between a bomb and an open space replace the corresponding 'O' with -1.<br>
<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: N = 3, M = 3, A[] = {{O, O, O}, {W, B, B}, {W, O, O}}<br>
&emsp;&emsp;Output: {{2, 1, 1}, {-1, 0, 0}, {-1, 1, 1}}<br>
&emsp;&emsp;Explanation: The walls at (1,0) and (2,0) are replaced by -1. The bombs at (1,1) and (1,2) are replaced by 0. The impact zone for the bomb at &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;(1,1) includes open spaces at index (0,0), (0,1) and (2,1) with distance from bomb calculated as 2,1,1 respectively.The impact &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;zone for the bomb at (1,2) includes open spaces at index (0,3) and (2,2) with distance from bomb calculated as 1,1 respectively.<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: N = 2, M = 2, A[] = {{O, O}, {O, O}} <br>
&emsp;&emsp;Output: {{-1, -1}, {-1, -1}<br>
<br>
<br>
Your Task:<br>  
You don't need to read input or print anything. Complete the function findDistance() which takes the matrix A[], M, and N as input parameters and the resultant matrix<br>
<br>
Expected Time Complexity: O(M*N)<br>
Expected Auxiliary Space: O(M*N)<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ N*M ≤ 10^6<br>
<br></p>
