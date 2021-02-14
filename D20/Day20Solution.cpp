class Solution{

    public:
    vector<int> ans;
    
    Node* search(Node* root, int target)
    {
        queue<Node*> q;
        q.push(root);
        while(!q.empty())
        {
            Node* temp = q.front();
            if(temp->data == target)
            {
                return temp;
            }
            if(temp->left)
            {
                q.push(temp->left);
            }
            if(temp->right)
            {
                q.push(temp->right);
            }
            q.pop();
        }
        return NULL;
    }

    void sumkdistanceNodeDown(Node *root, int k) 
    { 
         
        if (root == NULL || k < 0)  
            return; 
        if (k == 0) 
        { 
            ans.push_back(root->data); 
            return;
        }
        sumkdistanceNodeDown(root->left, k-1); 
        sumkdistanceNodeDown(root->right, k-1); 
    }
      
    int sumkDistanceNode(Node* root, Node* target , int k) 
    { 
        if (root == NULL) 
            return -1; 
      
        if (root == target) 
        { 
            sumkdistanceNodeDown(root, k); 
            return 0; 
        } 
      
        int dl = sumkDistanceNode(root->left, target, k); 
      
        if (dl != -1) 
        { 
             if (dl + 1 == k) 
                ans.push_back(root->data);
             else
                sumkdistanceNodeDown(root->right, k-dl-2); 
             return 1 + dl; 
        } 
      
        int dr = sumkDistanceNode(root->right, target, k); 
        if (dr != -1) 
        { 
             if (dr + 1 == k) 
                ans.push_back(root->data); 
             else
                sumkdistanceNodeDown(root->left, k-dr-2); 
             return 1 + dr; 
        } 
        return -1; 
    } 
    
    int sum_at_distK(Node* root, int target, int k)
    {
       if(!root)
        {
            return 0;
        }
        Node * targetNode = search(root,target);
        if(!targetNode)
        {
            return 0;
        }
        for(int i = 1;i<=k;i++)
        {
            sumkDistanceNode(root, targetNode, i);
        }

        int value = target;
        for(auto x:ans)
        {
            value += x;
        }
        return value;
    }
};
