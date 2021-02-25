<h1>Escape the Forbidden Forest</h1>
<p><br>
Penelope and her classmates are lost in the Forbidden Forest and the Devil is out to get them. But Penelope has magical powers that can build bridges across the dangerous river and take her friends to safety. The only bridges that can withstand the Devil's wrath are the ones built between two similar trees in the forest. 
Given str1 and str2 denoting the order of trees on either side of the river, find the maximum number of bridges that Penelope can build and save everyone from the Devil.<br> 
Note: Each tree in the forest belongs to one of the 3 categories represented by * or # or @<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: str1 = "*@#*", str2 = "*#"<br>
&emsp;&emsp;Output: 2<br>
&emsp;&emsp;Explanation: str1 = "*@#*" and str2 = "*#"<br> 
&emsp;&emsp;&emsp;&emsp;&emsp;Two bridges can be built between the banks of the river in the following manner.<br> 
&emsp;&emsp;&emsp;&emsp;&emsp;* @ # *<br>
&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;&emsp;|<br>
&emsp;&emsp;&emsp;&emsp;&emsp;*&emsp;&emsp;&emsp;#<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: str1 = "***", str2 = "##"<br>
&emsp;&emsp;Output: 0<br>
<br>
Your Task:<br>
You don't need to read input or print anything. Complete the function build_bridges() that takes str1 and str2 as input parameters and returns the maximum number of bridges that can be built. <br>
<br>
Expected Time Complexity: O(N*M)<br>
Expected Auxiliary Space: O(N*M)<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ N, M ≤ 100<br>
&emsp;&emsp;&emsp;&emsp;Where, N and M are the size of the string str1 and str2 respectively.<br>
<br></p>
