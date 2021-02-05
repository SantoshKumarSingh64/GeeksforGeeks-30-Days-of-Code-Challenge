<h1>Secret Cipher</h1>
<p><br>
Geek wants to send an encrypted message in the form of string S to his friend Keeg along with instructions on how to decipher the message. To decipher the message, his friend needs to iterate over the message string from left to right, if he finds a '*', he must remove it and add all the letters read so far to the string. He must keep on doing this till he gets rid of all the '*'.<br>
Can you help Geek encrypt his message string S? <br>
<br>
Note: If the string can be encrypted in multiple ways, find the smallest encrypted string. <br>
<br>
Example 1:<br>
&emsp;&emsp;Input: S = "ababcababcd"<br>
&emsp;&emsp;Output: ab*c*d<br>
&emsp;&emsp;Explanation: We can encrypt the string in following way : "ababcababcd" -> "ababc*d" -> "ab*c*d"<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: S = "zzzzzzz"<br>
&emsp;&emsp;Output: z*z*z<br>
&emsp;&emsp;Explanation: The string can be encrypted in 2 ways: "z*z*z" and "z**zzz". Out of the two "z*z*z" is smaller in length.<br>
<br>
Your Task:<br> 
You don't need to read input or print anything. Complete the function secretCipher() which takes the message string S as input parameter and returns the shortest possible encrypted string.<br>
<br>
Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(N)<br>
<br>
Constraints:<br> 
&emsp;&emsp;1 ≤ |S| ≤ 10^5<br>
<br></p>
