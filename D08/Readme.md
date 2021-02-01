<h1>Dam of Candies</h1>
<p><br>
Geek wants to make a special space for candies on his bookshelf. Currently, it has N books of different heights and unit width. Help him select 2 books such that he can store maximum candies between them by removing all the other books from between the selected books. The task is to find out the area between 2 books that can hold the maximum candies without changing the original position of selected books. <br>
<br>
Example 1:<br>
&emsp;&emsp;Input: N = 3, height[] = {1, 3, 4}<br>
&emsp;&emsp;Output: 1<br>
&emsp;&emsp;Explanation:<br>
&emsp;&emsp;&emsp;&emsp;1. Area between book of height 1 and book of height 3 is 0 as there is no space between them.<br>
&emsp;&emsp;&emsp;&emsp;2. Area between book of height 1 and book of height 4 is 1 by removing book of height 3.<br>
&emsp;&emsp;&emsp;&emsp;3. Area between book of height 3 and book of height 4 is 0 as there is no space between them.<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: N = 6, height[] = {2, 1, 3, 4, 6, 5}<br>
&emsp;&emsp;Output: 8<br>
&emsp;&emsp;Explanation: We remove the 4 books in the middle creating length = 4 for the candy dam. Height for dam will be min(2,5) = 2. Area between book of height 2 and book of height 5 is 2 x 4 = 8.<br>
<br>
Your Task:<br>  
You don't need to read input or print anything. Complete the function maxCandy() which takes the array height[] and size of array N as input parameters and returns the maximum candies geek can store<br>
<br>
Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(1)<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ N ≤ 10^5<br>
<br></p>
