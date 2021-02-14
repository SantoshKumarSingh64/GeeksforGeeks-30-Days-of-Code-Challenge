class Solution{
    public:
    int candies(int m, int n) 
    { 
    	// Your code goes here
    	int length = m*n;
    	bool arr[length+1];
    	for(int i=0;i<=length;i++)
    	    arr[i] = false;
    	arr[0] = true;
    	int count = -1;
    	for(int i=0;i<=length;i++)
    	{
    	    if(arr[i])
    	    {
    	        count++;
    	        if(i+m <= length)
    	            arr[i+m] = true;
    	        if(i+n <= length)
    	            arr[i+n] = true;
    	    }
    	}
    	return (length-count);
    } 
};
