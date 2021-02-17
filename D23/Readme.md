<h1>Lucy's Neighbours</h1>
<p><br>
Lucy lives in house number X. She has a list of N house numbers in the society. Distance between houses can be determined by studying the difference between house numbers. Help her find out K's closest neighbors.<br>
Note: If two houses are equidistant and Lucy has to pick only one, the house with the smaller house number is given preference.<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: N = 4, X = 0, K = 4, a[] = {-21, 21, 4, -12, 20}<br> 
&emsp;&emsp;Output: -21 -12 4 20<br>
&emsp;&emsp;Explanation: The closest neighbour is house number 4. Followed by -12 and 20. -21 and 21 are both equal distance from X=0. Therefore, Lucy can only pick 1. Based on the given condition she picks -21 as it is the smaller of the two. <br>
<br>
Example 2:<br>
&emsp;&emsp;Input: N = 6, X = 5, K = 3, a[] = {10, 2, 14, 4, 7, 6}<br>
&emsp;&emsp;Output: 4 6 7 <br>
<br>
Your Task:<br>  
You don't need to read input or print anything. Complete the function  Kclosest() which takes the array arr[], size of array N, X, and K as input parameters, and returns the list of numbers<br>
<br>
Expected Time Complexity: O(NlogN)<br>
Expected Auxiliary Space: O(N)<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ K ≤ N ≤ 10^5<br> 
&emsp;&emsp;-10^4 ≤ X, arr[i] ≤ 10^4<br>
<br></p>
