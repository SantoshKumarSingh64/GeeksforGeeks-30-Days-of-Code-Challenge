class Solution{
    public:
    int index = 0;
	int search(int arr[], int x, int n) 
    { 
    	for (int i = 0; i < n; i++) 
    		if (arr[i] == x) 
    			return i; 
    	return -1; 
    }
    
    void getPostOrder(int in[], int pre[], int n, int post[]) 
    { 
    	int root = search(in, pre[0], n);
    	if(root == -1)
    	    return;
        if (root != 0) 
    		getPostOrder(in, pre + 1, root, post); 
        if (root != n - 1) 
    		getPostOrder(in + root + 1, pre + root + 1, n - root - 1, post); 
        post[index] = pre[0];
        index++;
    } 
    
    bool checktree(int preorder[], int inorder[], int postorder[], int N) 
    { 
        int post[N];
        getPostOrder(inorder,preorder,N,post);
        for(int i=0;i<N;i++)
        {	
            if(post[i] != postorder[i])
                return false;
        }
        return true;
	} 
};
