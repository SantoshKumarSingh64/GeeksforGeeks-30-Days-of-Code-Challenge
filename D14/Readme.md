<h1>Ruling Pair</h1>
<p><br>
Geek Land has a population of N people and each person's ability to rule the town is measured by a numeric value arr[i]. The two people that can together rule Geek Land must be compatible with each other i.e., the sum of digits of their ability arr[i] must be equal. Their combined ability should be maximum amongst all the possible pairs of people. Find the combined ability of the Ruling Pair.<br>
<br>
Example 1:<br>
Input: N = 5, arr[] = {55, 23, 32, 46, 88}<br>
Output: 101<br>
Explanation: All possible pairs that are compatible with each other are- (23, 32) with digit sum 5 and (55, 46) with digit sum 10. Out of these the maximum combined ability pair is (55, 46) i.e. 55 + 46 = 101<br>
<br>
Example 2:<br>
Input: N = 4, arr[] = {18, 19, 23, 15}<br>
Output: -1<br>
Explanation: No two people are compatible with each other.<br> 
<br>
Your Task:<br>  
You don't need to read input or print anything. Complete the function RulingPairâ€‹() which takes the array arr[] and size of array N as input parameters and returns the answer. If No two people are compatible with
each other then return -1.<br>
<br>
Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(N)<br>
<br>
<br>
<br>
Constraints:<br>
1 ≤ N ≤ 10^5 <br>
1 ≤ arr[i] ≤ 10^9<br>
<br></p>
