<h1>Number of minimum picks to get 'k' pairs of socks from a drawer</h1>
<p><br>
A drawer contains socks of n different colours. The number of socks available of ith colour is given by a[i] where a is an array of n elements. Tony wants to take k pairs of socks out of the drawer. However, he cannot see the colour of the sock that he is picking. You have to tell what is the minimum number of socks Tony has to pick in one attempt from the drawer such that he can be absolutely sure, without seeing their colours, that he will have at least k matching pairs.<br>
<br>
Example 1:<br>
&emsp;&emsp;Input: N = 4, a[] = {3, 4, 5, 3}, K = 6<br>
&emsp;&emsp;Output: 15<br>
&emsp;&emsp;Explanation: The worst case scenario, after 14 picks will be 3,3,3,3 or 3,1,5,3 where each number represents picks of socks of one colour. Hence, 15th pick will get the 5th pair for sure.<br>
<br>
Example 2:<br>
&emsp;&emsp;Input: N = 2, a[] = {4, 6}, K = 3<br>
&emsp;&emsp;Output: 7<br>
&emsp;&emsp;Explanation: The Worst case scenario after 6 picks can be 3,3 or 1,5 or 5,1 of each coloured socks. Hence 7th pick will ensure 3rd pair.<br>
<br>
<br>
Your Task:<br>  
You don't need to read input or print anything. Complete the function find_min() which takes the array a[], size of array N, and value K as input parameters and returns the minimum number of socks Tony has to pick. If it is not possible to pick then return -1.<br>
<br>
Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(1)<br>
<br>
<br>
Constraints:<br>
&emsp;&emsp;1 ≤ N ≤ 10^5 <br>
&emsp;&emsp;1 ≤ a[i] ≤ 10^6<br>
<br></p>
