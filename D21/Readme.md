<h1>Corona Vaccine</h1>
<p><br>
Geek has developed an effective vaccine for Corona virus and he wants each of the N houses in Geek Land to have access to it. Given a binary tree where each node represents a house in Geek Land, find the minimum number of houses that should be supplied with the vaccine kit if one vaccine kit is sufficient for that house, its parent house and it's immediate child nodes.<br>  
<br>
Example 1:<br>
&emsp;&emsp;Input:<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;1<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;2&emsp;&emsp;&emsp;&emsp;3<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;4<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;5<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;6<br>
<br>
&emsp;&emsp;Output: 2<br>
&emsp;&emsp;Explanation: The vaccine kits should be supplied to house numbers 1 and 5.<br>
<br>
Example 2:<br>
&emsp;&emsp;Input:<br>
<br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;1<br>
&emsp;&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;\<br>
&emsp;&emsp;&emsp;&emsp;2&emsp;&emsp;&emsp;&emsp;3 <br>
 <br>
&emsp;&emsp;Output: 1<br>
&emsp;&emsp;Explanation: The vaccine kits should be supplied to house number 1.<br>
<br>
Your Task:<br>
You don't need to read input or print anything. Complete the function supplyVaccine() which takes the root of the housing tree as input parameter and returns the minimum number of houses that should be supplied with the vaccine kit.<br>
<br>
Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(N)<br>
<br>
<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ N ≤ 10^5<br>
<br></p>
