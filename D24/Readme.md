<h1>Gadgets of Doraland</h1>
<p><br>
In Doraland, people have unique Identity Numbers called D-id. Doraemon owns the most popular gadget shop in Doraland. Since his gadgets are in high demand and he has only K gadgets left he has decided to sell his gadgets to his most frequent customers only. N customers visit his shop and D-id of each customer is given in an array array[ ]. In case two or more people have visited his shop the same number of time he gives priority to the customer with higher D-id. Find the D-ids of people he sells his K gadgets to.<br>
<br>
Example 1:<br>
Input: N = 6, array[] = {1, 1, 1, 2, 2, 3}, K = 2<br>
Output: 1 2<br>
Explanation: Customers with D-id 1 and 2 are most frequent.<br>
<br>
Example 2:<br>
Input: N = 8, array[] = {1, 1, 2, 2, 3, 3, 3, 4}, K = 2<br>
Output: 3 2<br>
Explanation: People with D-id 1 and 2 have visited shop 2 times Therefore, in this case, the answer includes the D-id 2 as 2 > 1.<br>
<br>
Your Task:<br>
You don't need to read input or print anything. Complete the function TopK() which takes array[ ] and integer K as input parameters and returns an array containing D-id of customers he has decided to sell his gadgets to.<br>
<br>
Expected Time Complexity: O(N)<br>
Expected Auxiliary Space: O(N)<br>
<br>
Constraints:<br>
1 ≤ N ≤ 10^5<br>
1 ≤ D-id ≤ 10^4<br>
<br><p>
