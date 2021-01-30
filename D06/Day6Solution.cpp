class Solution{
    
    public:
    int Maximum_Sum(vector<vector<int>> &mat,int N,int K){
        // Your code goes here
        for(int i=0;i<N;i++)
        {    
            mat[i].insert(mat[i].begin(),0);
            for(int j=2;j<=N;j++)
                mat[i][j] += mat[i][j-1];
        }
        
        int ans = 0;
        for(int x=N-K; x>-1; x--)
        {
            for(int y=N; y>K-1; y--)
            {
                int current_ans = 0;
                for(int temp=x; temp<x+K; temp++)
                {
                    current_ans += (mat[temp][y] - mat[temp][y-K]);
                }
                ans = max(ans,current_ans);
            }
        }
        return ans;
    }  
};
