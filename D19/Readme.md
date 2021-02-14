<h1>Restricted Pacman</h1>
<p><br>
In the game of Restricted Pacman, an infinite linear path is given. Pacman has to start at position 0 and eat as many candies as possible. In one move he can only jump a distance of either M or N.  If M and N are coprime numbers, find how many candies will be left on the board after the game is over.<br>
Note: The result is always finite as after a point X every index in the infinite path can be visited. <br>
<br>
Example 1:<br>
&emsp;&emsp;Input: M = 2, N = 5<br>
&emsp;&emsp;Output: 2<br>
&emsp;&emsp;Explanation: From index 0, the indices that can be visited are<br>
&emsp;&emsp;&emsp;&emsp;&emsp;0 + 2 = 2<br>
&emsp;&emsp;&emsp;&emsp;&emsp;0 + 2 + 2 = 4<br>
&emsp;&emsp;&emsp;&emsp;&emsp;0 + 5 = 5<br>
&emsp;&emsp;&emsp;&emsp;&emsp;0 + 2 + 2 + 2 = 6<br>
&emsp;&emsp;&emsp;&emsp;&emsp;0 + 2 + 5 = 7<br>
&emsp;&emsp;&emsp;&emsp;&emsp;0 + 2 + 2 + 2 + 2 = 8<br>
&emsp;&emsp;&emsp;&emsp;&emsp;0 + 2 + 2 + 5 = 9<br>
&emsp;&emsp;&emsp;&emsp;&emsp;0 + 5 + 5 = 10<br>
&emsp;&emsp;&emsp;&emsp;&emsp;and so on.<br>
&emsp;&emsp;&emsp;&emsp;&emsp;1 and 3 are the only indices that cannot be visited. Therefore the candies at these two positions will be left on the board.<br> 
<br>
Example 2:<br>
&emsp;&emsp;Input: M = 2, N = 7<br>
&emsp;&emsp;Output: 3 <br>
<br>
Example 3:<br>
&emsp;&emsp;Input: M = 25, N = 7<br>
&emsp;&emsp;Output: 72<br>
<br>
Your Task:<br>  
You don't need to read input or print anything. Complete the function candies() which take M and N as input parameters and return the answer.<br>
<br>
Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(N)<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ M, N ≤ 500<br>
<br></p>
