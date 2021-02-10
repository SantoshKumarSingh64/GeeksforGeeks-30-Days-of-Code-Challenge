<h1>Help Classmates</h1>
<p><br>
Professor X wants his students to help each other in the chemistry lab. He suggests that every student should help out a classmate who scored less marks than him in chemistry and whose roll number appears after him. But the students are lazy and they don't want to search too far. They each pick the first roll number after them that fits the criteria. Find the marks of the classmate that each student picks.<br>
<br>
Note: one student may be selected by multiple classmates.<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: N = 5, arr[] = {3, 8, 5, 2, 25}<br>
&emsp;&emsp;Output: 2 5 2 -1 -1<br>
&emsp;&emsp;Explanation: <br>
&emsp;&emsp;&emsp;&emsp;1. Roll number 1 has 3 marks. The first person who has less marks than him is roll number 4, who has 2 marks.<br>
&emsp;&emsp;&emsp;&emsp;2. Roll number 2 has 8 marks, he helps student with 5 marks.<br>
&emsp;&emsp;&emsp;&emsp;3. Roll number 3 has 5 marks, he helps student with 2 marks.<br>
&emsp;&emsp;&emsp;&emsp;4. Roll number 4 and 5 can not pick anyone as no student with higher roll number has lesser marks than them. This is denoted by -1.<br> 
&emsp;&emsp;&emsp;&emsp;&emsp;Output shows the marks of the weaker student that each roll number helps in order. ie- 2,5,2,-1,-1<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: N = 4, a[] = {1, 2, 3, 4}<br>
&emsp;&emsp;Output: -1 -1 -1 -1 <br>
&emsp;&emsp;Explanation: As the marks ars in increasing order. None of the students can find a classmate who has a higher roll number and less marks<br> 
&emsp;&emsp;&emsp;&emsp;&emsp;than them.<br>
<br>
Your Task:<br>  
You don't need to read input or print anything. Complete the function help_classmate() which takes the array arr[] and size of array N as input parameters and returns a list of numbers. If a student is unable to find anyone then output is -1.<br>
<br>
Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(N)<br>
<br>
<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ N ≤ 10^6<br>
<br></p>
