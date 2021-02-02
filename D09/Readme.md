<h1>Transfiguration</h1>
<p><br>
Professor McGonagall teaches transfiguration at Hogwarts. She has given Harry the task of changing himself into a cat. She explains that the trick is to analyze your own DNA and change it into the DNA of a cat. The transfigure spell can be used to pick any one character from the DNA string, remove it and insert it in the beginning. 
Help Harry calculates minimum number of times he needs to use the spell to change himself into a cat.
<br>
Example 1:<br>
&emsp;&emsp;Input: <br>
&emsp;&emsp;A = "GEEKSFORGEEKS"<br> 
&emsp;&emsp;B = "FORGEEKSGEEKS"<br>
&emsp;&emsp;Output: 3<br>
&emsp;&emsp;Explanation:The conversion can take place in 3 operations:<br>
&emsp;&emsp;&emsp;&emsp;1. Pick 'R' and place it at the front, A="RGEEKSFOGEEKS"<br>
&emsp;&emsp;&emsp;&emsp;2. Pick 'O' and place it at the front, A="ORGEEKSFGEEKS"<br>
&emsp;&emsp;&emsp;&emsp;3. Pick 'F' and place it at the front, A="FORGEEKSGEEKS"<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: <br>
&emsp;&emsp;A = "ABC" <br>
&emsp;&emsp;B = "BCA"<br>
&emsp;&emsp;Output: 2<br>
&emsp;&emsp;Explanation: The conversion can take place in 2 operations:<br>
&emsp;&emsp;&emsp;&emsp;1. Pick 'C' and place it at the front, A = "CAB"<br>
&emsp;&emsp;&emsp;&emsp;2. Pick 'B' and place it at the front, A = "BCA"<br>
<br>   
Your Task:<br>  
You don't need to read input or print anything. Complete the function transfigure() which takes strings A and B as input parameters and returns the minimum number of spells needed. If it is not possible to convert A to B then return -1.<br>
<br>
Expected Time Complexity: O(max(|A|, |B|))<br>
Expected Auxiliary Space: O(1)<br>
<br>
<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ |A|, |B| ≤ 10^5<br>
&emsp;&emsp;A and B consists of lowercase and uppercase letters of english alphabet only.<br>
<br></p>
