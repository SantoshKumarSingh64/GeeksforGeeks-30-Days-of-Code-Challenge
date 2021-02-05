class Solution{
    public:
    string compress(string s)
    {
        // Your code goes here
        int n = s.length();
        vector<int> v(n);
        for(int i=1;i<n;i++)
        {
            int j=v[i-1];
            while(j > 0 && s[i] != s[j])
            {
                j = v[j-1];
            }
            if(s[i]==s[j])
                j++;
            v[i] = j;
        }
        string ans;
        for(int i=n-1; i>=0; i--)
        {
            if(i%2)
            {
                if(v[i] >= (i+1)/2 && (i+1)%(2*(i+1-v[i]))==0)
                {
                    ans.push_back('*');
                    i/=2;
                    i++;
                }
                else
                {
                    ans.push_back(s[i]);
                }
            }
            else
            {
                ans.push_back(s[i]);
            }
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};

